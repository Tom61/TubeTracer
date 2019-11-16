from numpy import pi, arccos, tan


class BendedTube:

    def __init__(self, points=False):
        self.p = points
        if points:
            self._calc_()

    @staticmethod
    def length_of_line(p1, p2):
        length = 0
        for i in range(3):
            length += (p1[i] - p2[i]) ** 2
        return length ** 0.5

    def _calc_(self):
        # theoretical lengths from point to point
        self.theoretic_len = list((map(self.length_of_line, self.p[:], self.p[1:])))

        # lengths of ledger lines to solve cosin theorem in the next step
        self.ledger_len = list((map(self.length_of_line, self.p[:], self.p[2:])))

        # angle (in radians)  between lines. Calc. by cosin theorem
        self.angle = list(map(lambda a, b, c: arccos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)),
                              self.ledger_len, self.theoretic_len, self.theoretic_len[1:]))

        # bending angle (in degree)
        self.bending_angle = [(pi - angle) * 360 / 2 / pi for angle in self.angle]

        # bow lengths
        self.bow_len = list(map(lambda radius, bend_angle: 2 * pi * radius / 360 * bend_angle,
                                [point[3] for point in self.p[:] if point[3] > 0], self.bending_angle))

        # "cut off" or "over length" (from tangent point to coordinate point)
        self.over_len = list(map(lambda radius, angle: radius / tan(angle / 2),
                                 [point[3] for point in self.p[:] if point[3] > 0], self.angle))

        # calc the true lengths of the straights
        self.real_len = self.theoretic_len.copy()
        for i in range(len(self.over_len)):
            self.real_len[i] -= self.over_len[i]
            self.real_len[i + 1] -= self.over_len[i]

        # calc the total length
        self.len_sum = sum(self.real_len) + sum(self.bow_len)

    def set_points(self, points):
        self.p = points
        self._calc_()
        return

    def get_total_length(self):
        return self.len_sum

    def get_straight_lengths(self):
        return self.real_len

    def get_bow_lengths(self):
        return self.bow_len

    def get_bending_angles(self):
        return self.bending_angle

    def get_result_set(self):
        return self.len_sum, self.real_len, self.bow_len, self.bending_angle
