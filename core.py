class HouseBadge:
    def __init__(self, num, name):
        self._num = num
        self._name = name

    def __eq__(self, other):
        return isinstance(other, HouseBadge) and self._num == other._num


class Track:
    def __init__(self, house_list):
        self._list = house_list
        self._cycle_num = 0
        self._cur_house = 0
        self._count = len(house_list)

    def renew_order(self, house_list):
        self._list = house_list
        self._cycle_num = 0
        self._cur_house = 0
        self._count = len(house_list)

    def new_cycle(self):
        self._cycle_num = 1
        self._cur_house = 0

    def next(self):
        pass

    def next_with_pass(self):
        pass


class TrackBoard:
    def __init__(self, edition, addon, player_count):
        if edition == 1:
            pass
        if edition == 2:
            if addon == 0:
                throne_list = [1, 2, 3]
                if player_count > 3:
                    throne_list.append(4)
                if player_count > 4:
                    throne_list.append(5)
                    if player_count > 5:
                        throne_list.append(6)
                self._throne_track = Track(throne_list)


class HouseTimer:
    def __init__(self):
        # in seconds
        self._main_pool = 0
        self._reserve_pool = 20 * 60

    def tick(self):
        if self._main_pool > 0:
            self._main_pool -= 1
        else:
            self._reserve_pool -= 1

        return self._main_pool, self._reserve_pool


class Board:
    def __init__(self, edition, addon, player_count):
        # state
        self._round = 1
        self._phase = 1
        # 0 - not started
        # 1 - in progress
        # 2 - paused
        # 3 - game over
        self.app_state = 0

        # time (in seconds)
        self._overall_time = 0
        self._game_time = 0 # without pause time

        # houses
        if edition == 1:
            pass
        if edition == 2:
            if addon == 0:
                house_list = [1, 2, 3]
                if player_count > 3:
                    house_list.append(4)
                if player_count > 4:
                    house_list.append(5)
                    if player_count > 5:
                        house_list.append(6)

        # tracks
        # self._track_board =