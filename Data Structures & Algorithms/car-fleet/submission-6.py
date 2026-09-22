class Solution:

    def carFleet(
        self, target: int, position: List[int], speed: List[int]
    ) -> int:
        # Pair position with speed, sorted by position in descending order
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        max_time = 0.0

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            # If a car takes longer than the fleet ahead of it,
            # it forms a new fleet. Otherwise, it merges.
            if time_to_target > max_time:
                fleets += 1
                max_time = time_to_target

        return fleets