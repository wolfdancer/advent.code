from __future__ import annotations


class IndicatorLights:
    def __init__(self, pattern: str) -> None:
        self.pattern: str = pattern
        self.states: list[str] = [ch for ch in pattern if ch in ('.', '#')]
        self._hash: int = 0
        for state in self.states:
            self._hash *= 2
            if state == '#':
                self._hash += 1

    def reset(self) -> IndicatorLights:
        return IndicatorLights('.' * len(self.states))

    def press(self, buttons: list[int]) -> IndicatorLights:
        new_states = list(self.states)
        for index in buttons:
            new_states[index] = '#' if new_states[index] == '.' else '.'
        return IndicatorLights(''.join(new_states))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IndicatorLights) and self._hash == other._hash

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return f"IndicatorLights({self.pattern})"


class Buttons:
    def __init__(self, values: list[int]) -> None:
        self.values: list[int] = values

    def __repr__(self) -> str:
        return f"Buttons({self.values})"


def process(target: IndicatorLights, button_lists: list[Buttons]) -> int:
    initial: IndicatorLights = target.reset()
    presses: dict[IndicatorLights, list[Buttons]] = {initial: []}
    while True:
        next_presses: dict[IndicatorLights, list[Buttons]] = dict(presses)
        for state, entry_value in presses.items():
            for button_list in button_lists:
                next_state: IndicatorLights = state.press(button_list.values)
                if next_state in next_presses:
                    continue
                value: list[Buttons] = entry_value + [button_list]
                next_presses[next_state] = value
                if next_state == target:
                    return len(value)
        presses = next_presses
