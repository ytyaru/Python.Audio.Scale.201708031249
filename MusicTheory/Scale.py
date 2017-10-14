#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
import EqualTemperament
import Key
class Scale:
    def __init__(self):
        self.__major = [2,2,1,2,2,2,1]
        self.__minor = [2,1,2,2,1,2,2]
        self.__scales = []
        self.__et = EqualTemperament.EqualTemperament()
    @property
    def Scales(self): return self.__scales
    @property
    def Key(self): return self.__scales[0]
    
    # ドレミファソラシド(C,D,E,F,G,A,B)
    def Major(self, key='C'): return self.__create_scales(self.__major, key)
    def Minor(self, key='C'): return self.__create_scales(self.__minor, key)
    def __create_scales(self, scales, key):
        self.__scales.clear()
        k = Key.Key()
        pitch = k.Get(key)
        self.__scales.append(pitch)
        for interval in scales:
            #0-11
            #-1-->11
            #-2-->10
            #12-->0
            #13-->1
            pitch += interval
            if pitch < 0: pitch = len(self.__et.Keys) - abs(pitch)
            elif len(self.__et.Keys)-1 < pitch: pitch %= len(self.__et.Keys)
            self.__scales.append(pitch)
#        print('self.__scales:', self.__scales)
        return self.__scales


if __name__ == '__main__':
    s = Scale()
    """
    print(s.Major(key='C'))
    print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print(s.Minor(key='A'))
    print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print(s.Minor(key='C'))
    print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print(s.Major(key='D'))
    print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    """
    print('---------- メジャー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        print(s.Major(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print('---------- マイナー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(s.Minor(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
