class Perceptron:
    def __init__(self):
        self.x = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.n = [0.02, 0.05, 0.4]
        self.w = [0.1, 0.2, 0.3]
        self.O = 0.2
        self.t = self._true_values_calc()
        self.result_of_learning = self._learning(self.x, self.w, self.t, self.n[2])

    def _true_values_calc(self) -> list:
        """
        initialization of T
        :return: list T-items
        """
        t = []
        for i in self.x:
            t.append(
                self._logical_func(i[0], i[1], i[2])
            )
        return t

    @staticmethod
    def _logical_func(x1, x2, x3):
        """
        Calculation of true value using logical function
        :param x1, x2, x3: image
        :return: Boolean value is calculated by a logical function
        """
        if (not x1 or x2) and x3:
            return True
        return False

    def _learning(self, Xs: list, Ws: list, Ts: list, n: float) -> str:
        """
        Learning perceptron, auto correction of weight coefficients
        :param Xs: image list
        :param Ws: weighting factors list
        :param Ts: true values
        :param n: rate of learning
        :return: the result of training in a str
        """
        result = ""
        for x in Xs:
            index = Xs.index(x)
            j = 3; a = 0; T = Ts[index]

            # calculate a
            while j:
                j -= 1
                a += x[j] * Ws[j]

            # calculate result
            Y = 1 if a >= self.O else 0
            sigma = T - Y
            a = round(a, 1)

            result += f"w1={Ws[0]} | w2={Ws[1]} | w3={Ws[2]} | O={self.O} | x1={x[0]} | x2={x[1]} | x3={x[2]} | "\
                      f"a={a} | Y={Y} | T={T} | n(T-Y)={n*sigma} | sigma*w1={sigma*Ws[0]} | sigma*w2={sigma*Ws[1]} | " \
                      f"sigma*w3={sigma*Ws[2]} | sigma*O={sigma*self.O}\n"

            # adjustment of weighting factors
            if Y != T:
                delta = []; j = 0

                # calculate delta
                while j < 3:
                    delta.append(n * x[j] * sigma)
                    j += 1

                j = 0
                while j < 3:
                    Ws[j] = round(Ws[j] + delta[j], 1)
                    j += 1
        return result


if __name__ == "__main__":
    neuron = Perceptron()
    print(neuron.result_of_learning)

