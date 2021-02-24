import math


class OkumaraHataModel:
    def __init__(self, carrierFrequency, heightTransmitter, heightReceiver, linkDistance, city, area):
        self.carrierFrequency = carrierFrequency
        self.heightTransmitter = heightTransmitter
        self.heightReceiver = heightReceiver
        self.linkDistance = linkDistance
        self.city = city
        self.area = area
        self.correctionFactor = 0.0
        self.antennaCorrectionFactor()
        self.pathLoss = 0.0
        self.getPathLoss()
        self.countLossVariance()

    def antennaCorrectionFactor(self):
        if self.city == 1:
            self.correctionFactor = (0.8 + ((1.1 * math.log10(self.carrierFrequency) - 0.7)
                                            * self.heightReceiver) - (1.56 * math.log10(self.carrierFrequency)))

        else:
            if (self.carrierFrequency >= 150) and (self.carrierFrequency <= 200):
                self.correctionFactor = (8.29 * (math.pow(math.log10(1.54 * self.heightReceiver), 2))) - 1.1
            else:
                self.correctionFactor = (3.2 * (math.pow(math.log10(11.75 * self.heightReceiver), 2))) - 4.97

    def getPathLoss(self):
        self.pathLoss = 69.55 + (26.16 * math.log10(self.carrierFrequency)) - (13.82 * math.log10(self.heightTransmitter)) - self.correctionFactor + ((44.9 - (6.55 * math.log10(self.heightTransmitter)))
             * math.log10(self.linkDistance))

    def countLossVariance(self):
        differenceLoss = 0.0
        if self.area == 1:
            differenceLoss = 2 * math.pow(math.log10((self.carrierFrequency / 28)), 2) + 5.4

        elif self.area == 2:
            differenceLoss = 4.78 * math.pow(math.log10(self.carrierFrequency), 2) - 18.33 * math.log10(self.carrierFrequency) + 40.94

        self.pathLoss -= differenceLoss