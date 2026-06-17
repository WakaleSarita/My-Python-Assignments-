### Write a program to input any alphabet and check whether it is vowel or consonant.

# Take input from user.

alphabet = input('Enter Alphabet : ')

# perform condition and display result.

if(alphabet in ' aeiouAEIOU'):
    print('Alphabet is vowel.')
else:
    print('Alphabet is consonant.')