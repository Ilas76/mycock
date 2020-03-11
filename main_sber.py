from sber_for_nude import sberbank

import pickle
import time

def main():
    while True:
        try:
            value = sberbank()
            with open('value.txt', 'wb') as f:
                    pickle.dump(value, f)
            time.sleep(60)
        except Exception:
            pass

if __name__ == '__main__':
	main()