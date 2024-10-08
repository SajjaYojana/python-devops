sample_str = "This-is-a-sample-string"
print(sample_str)

#How to access individual elements from a string
#using index and it starts from zero
print(sample_str[8])

#Slicing
sub_str = sample_str[2:7]
print(sub_str)

sub_str = sample_str[:]
print(sub_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str)

# REverse a string
sub_str = sample_str[::-1]
print("Reversed String:", sub_str)

#Length of a string
len_str = len(sample_str)
print("Length of a string:", len_str)

