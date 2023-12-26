from typing import Any
from day import Day
from aocd import submit
from collections import deque, defaultdict
from math import lcm


class Module(tuple):
    def __init__(self, target):
        self.state = None
        self = tuple(target)

    def __repr__(self):
        return f"{self.__class__.__name__}(target:{super().__repr__()} state:{self.state})"


class BroadCaster(Module):
    pass


class FlipFlop(Module):
    def __init__(self, target):
        super().__init__(target)
        self.state: bool = False

    def __bool__(self):
        return self.state

    def __call__(self, pulse):
        if pulse:
            return (None,), None
        self.state = not self.state
        return tuple(self), self.state


class Conjunction(Module):
    def __init__(self, target):
        super().__init__(target)
        self.state = {}

    def __bool__(self):
        if self.state:
            return not all(self.state.values())
        return False

    def add_sender(self, sender):
        self.state[sender] = False

    def __call__(self, sender, pulse):
        self.state[sender] = pulse
        return tuple(self), bool(self)


class PulsePropagator:
    def __init__(self, data):
        self._raw_data = data
        self.num_pulses = [0, 0]
        self.graph = {}
        self._parse_graph()
        self.reset_queue()
        self.target_nodes = dict()

    def reset_queue(self):
        # Sender, Receiver, High/Low Pulse
        self.queue = deque([("button", "broadcaster", False)])
        self.target_pulses = defaultdict(list)

    def _parse_graph(self):
        # Parse objects to graph
        for line in self._raw_data:
            sender, target = line.split(" -> ")
            receivers = target.split(", ")

            if sender.startswith("broadcaster"):
                obj = BroadCaster(receivers)
            elif sender.startswith("&"):
                sender = sender[1:]
                obj = Conjunction(receivers)
            elif sender.startswith("%"):
                sender = sender[1:]
                obj = FlipFlop(receivers)
            self.graph[sender] = obj

        # Add senders to conjunctions
        for sender, obj in self.graph.items():
            for receiver in obj:
                if isinstance(self.graph.get(receiver, None), Conjunction):
                    self.graph[receiver].add_sender(sender)
        del self._raw_data

    def run_pulse(self):
        while self.queue:
            sender, receiver, pulse = self.queue.popleft()

            if pulse is None:
                continue

            if receiver in self.target_nodes and self.target_nodes[receiver] is None:
                self.target_pulses[receiver].append(pulse)

            # print(sender, ["-low", "-high"][pulse], "->", receiver)

            self.num_pulses[pulse] += 1

            if isinstance(self.graph.get(receiver, None), FlipFlop):
                ping = self.graph[receiver](pulse)
                next_target, next_pulse = ping
            elif isinstance(self.graph.get(receiver), Conjunction):
                next_target, next_pulse = self.graph[receiver](sender, pulse)
            elif receiver in self.graph:
                next_target = self.graph[receiver]
                next_pulse = pulse
            else:
                continue

            for target in next_target:
                self.queue.append((receiver, target, next_pulse))
        return self.num_pulses

    def button(self, iterations=1):
        for _ in range(iterations):
            self.reset_queue()
            self.run_pulse()
        return self.num_pulses

    @property
    def value(self):
        return self.num_pulses[1] * self.num_pulses[0]

    def find_low_pulse(self, target="rx"):
        # Find input nodes to target
        for _, obj in self.find_input():
            # The input to rx is a single conjunction
            # We can massage the conditions to find the first low pulse
            if isinstance(obj, Conjunction):
                for k in obj.state.keys():
                    self.target_nodes[k] = None

        counter = 0
        while True:
            self.button()
            counter += 1

            # Check if we found any targets
            for k, v in self.target_pulses.items():
                if not all(v) and self.target_nodes[k] is None:
                    self.target_nodes[k] = counter
                    print(f"Found {k} at {counter}")

            # Check if we found all targets and calc least common multiple
            if all(self.target_nodes.values()):
                return lcm(*self.target_nodes.values())

    def find_input(self, target="rx"):
        inputs = []
        for name, node in self.graph.items():
            if target in node:
                inputs.append((name, node))
        return inputs


def main(day, part=1):
    propagator = PulsePropagator(day.data)
    if part == 1:
        propagator.button(1000)
        return propagator.value
    if part == 2:
        return propagator.find_low_pulse()


if __name__ == "__main__":
    day = Day(20)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=20, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=20, year=2023)
