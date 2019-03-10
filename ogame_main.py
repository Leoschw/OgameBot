import cycles
import classes as c
import traceback


while True:

    cycles.logInAccount('leo.schwab@gmx.net', 'ls--1989')
    try:
        cycles.buildMinesCycle()
    except Exception:
        traceback.print_exc()
        continue


