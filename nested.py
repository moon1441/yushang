#!/usr/bin/env python
# encoding:utf-8


def nested(p1,p2):
    p1.sort();
    p2.sort();
    print(p1)
    print(p2)
    #set an remark ,for at most one element of p1 between two neighboring elements of p2
    remark=False
    #set interval begin & end
    begin=p2.pop(0)
    end = begin

    if isinstance(begin,float) is not True:
            raise TypeError("p2 has a no float %s" % begin)
    
    while len(p1)>0:
        e1 = p1.pop(0)

        if isinstance(e1,float) is not True:
            raise TypeError("p1 has a no float value %s" % e1)

        #p1 p2 can not have same value
        if e1 == begin:
            return None
        
        while len(p2)>0:
            end = p2.pop(0)

            if isinstance(end,float) is not True:
                raise TypeError("p2 has a no float value %s" % end )

            #p1 p2 can not have same value
            if e1 == end:
                return None

            if e1<end and e1>begin:
                #move forward
                begin = end
                break
            elif  e1<begin:
                return False
            elif e1>end:
                begin = end
                continue
            
        if  len(p2) == 0:
            if len(p1)>0:
                return False  
            if e1>end:
                return False
    return True

def main():
    test_p1=[4.0,1.5]
    test_p2=[2.0,1.0,3.0,5.0]
    print(nested(test_p1,test_p2)) # True

    test_p1=[4.0,4.1,1.5]
    test_p2=[2.0,1.0,3.0,5.0]
    print(nested(test_p1,test_p2)) # Fasle

    test_p1=[4.0,3.0,1.5]
    test_p2=[2.0,1.0,3.0,5.0]
    print(nested(test_p1,test_p2)) # None

    test_p1=[0.5,4.5]
    test_p2=[2.0,1.0,3.0,5.0]
    print(nested(test_p1,test_p2)) # False

    test_p1=[1.5,5.5]
    test_p2=[2.0,1.0,3.0,5.0]
    print(nested(test_p1,test_p2)) # False

if __name__ == "__main__":
    main()