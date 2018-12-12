
class Perceptron:
    def __init__(self):
        self.x = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.n = [0.02, 0.05, 0.4]
        self.w = [0.1, 0.2, 0.3]  # вагові коеф
        self.O = 0.2  # порогове значення
        self.t = []

        for i in self.x:
            self.t.append(
                self.log_func(i[0], i[1], i[2])
            )
        print(self.l(self.x, self.w, self.t, self.n[2]))

    def l(self, Xs, Ws, Ts, n):
        step = 0
        result = ''
        cont = True
        while cont:
            step += 1
            result += f"Step #{step}\n"
            i = 0
            while i < len(Xs):
                a = 0
                a += Xs[i][0] * Ws[0] + Xs[i][1] * Ws[1] + Xs[i][2] * Ws[2]
                Y = True if a >= self.O else False

                result += f"w1={round(Ws[0], 1)} | " \
                          f"w2={round(Ws[1], 1)} | " \
                          f"w3={round(Ws[2], 1)} | " \
                          f"x1={Xs[i][0]} | x2={Xs[i][1]} | x3={Xs[i][2]} | " \
                          f"a={a} | Y={Y} | T={Ts[i]} | n(T-Y)={n*(Ts[i]-Y)} | " \
                          f"bw1={round((Ts[i]-Y)*Ws[0], 1)} | " \
                          f"bw2={round((Ts[i]-Y)*Ws[1], 1)} | " \
                          f"bw3={round((Ts[i]-Y)*Ws[2], 1)}\n"

                # Корегування вагових коефіцієнтів
                if Y != Ts[i]:
                    k = 0
                    while k < 3:
                        Ws[k] = Ws[k] + (n * (Ts[i] - Y) * Xs[i][k])
                        k += 1
                else:
                    cont = False
                i += 1
            result += "\n\n"
        return result


    def learn(self, Xs, Ws, Ts, n):
        result = ''
        cont = True
        step = 0
        while cont:
            i = 0
            step += 1
            result += f"Step #{step}\n"
            while i < len(Xs):
                a = j = 0
                while j < 3:
                    a += round((Xs[i][j] * Ws[j]), 1)
                    j += 1

                Y = True if a >= self.O else False

                result += f"w1={round(Ws[0], 1)} | " \
                          f"w2={round(Ws[1], 1)} | " \
                          f"w3={round(Ws[2], 1)} | " \
                          f"x1={Xs[i][0]} | x2={Xs[i][1]} | x3={Xs[i][2]} | " \
                          f"a={a} | Y={Y} | T={Ts[i]} | n(T-Y)={n*(Ts[i]-Y)} | " \
                          f"bw1={round((Ts[i]-Y)*Ws[0], 1)} | " \
                          f"bw2={round((Ts[i]-Y)*Ws[1], 1)} | " \
                          f"bw3={round((Ts[i]-Y)*Ws[2], 1)}\n"

                # Корегування вагових коефіцієнтів
                if Y != Ts[i]:
                    k = 0
                    while k < 3:
                        Ws[k] = Ws[k] + (n * (Ts[i] - Y) * Xs[i][k])
                        k += 1
                else:
                    cont = False
                i += 1
            result += "\n\n"

        return result

    @staticmethod
    def log_func(x1, x2, x3):
        # (|x1 V x2) A x3  =
        # = (x3 A |x1) V (x3 A x2) // дистрибутивність
        # if (x3 and not x1) or (x3 and x2):

        if (not x1 or x2) and x3:
            return True
        return False


Perceptron()
