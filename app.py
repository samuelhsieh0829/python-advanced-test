from mod import moduleA
import logging

logging.basicConfig(level=logging.INFO)

def main(A, B, C):
    obj1 = moduleA(A)
    obj2 = moduleA()
    for i in range(B):
        obj1.methodA()
        obj2.methodA()
    obj1.methodB()
    obj2.methodB()
    obj1.methodC(C)
    obj2.methodC()

if __name__ == "__main__":
    score = 0

    tests = [(2, 2, 3),
             (1, 1, 1),
             (1, 0, 1)]
    
    for test in tests:
        try:
            main(*test)
            score += 1
            logging.info(f"\x1b[32m{test} pass\x1b[0m")
        except:
            logging.exception(f"\x1b[31m{test} failed:\x1b[0m")
        finally:
            print("----------------------")

    logging.info(f"\x1b[35mTest completed, score:\x1b[33m{score}\x1b[0m")