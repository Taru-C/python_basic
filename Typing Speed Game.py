import time

sentence = "Python is fun"

print("Type this sentence:")
print(sentence)

input("Press Enter when ready...")

start = time.time()

typed = input("\nType here: ")

end = time.time()

time_taken = end - start

print("\nTime taken:", round(time_taken, 2), "seconds")

if typed == sentence:
    print("Correct! ✅")
else:
    print("Wrong typing ❌")