from math import exp

class Neuron:
    def __init__(self, ws: list, n: float, tolerance: float, c: float):
        self.ws = ws
        self.n = n
        self.tolerance = tolerance
        self.c = c

    def _get_net(self, xs: list) -> float:
        if len(self.ws) != len(xs):
            Exception("Кількість вагових коефіцієнтів W має бути рівною кількості вхідних аргументів X")
        net = 0
        for i in range(0, len(self.ws)):
            net += self.ws[i] * int(xs[i])
        return net

    def _update_w(self, delta_w: list):
        for i in range(0, len(self.ws)):
            self.ws[i] += delta_w[i]

    def _f(self, net):
        return (2.0 / (1 + exp(-self.n * net))) - 1

    def _f_derived(self, net):
        return (2 * self.n * exp(-self.n * net)) / (pow((1 + exp(-self.n * net)), 2))

    def _w_correction(self, d: int, o: float, net: float, xs: list) -> list:
        delta_ws = []
        for x in xs:
            delta_ws.append(self.c * (d - o) * self._f_derived(net) * x)
        return delta_ws

    def _error(self, d: int, o: float):
        return 0.5 * (d - o)**2

    def train(self, xs: list, train_d: int):
        net = self._get_net(xs)
        o = self._f(net)

        E = self._error(train_d, o)
        print(f"o: {round(o)}, d: {train_d}, E: {round(E, 2)}")
        if E >= self.tolerance:
            self._update_w(self._w_correction(train_d, o, net, xs))
            print("Нейрон тупий")
            return -1
        else:
            print("Нейрон розумний")
            return 1
    def think(self, xs):
        net = self._get_net(xs)
        o = self._f(net)

        print(f"o: {round(o)}")
        return round(o)