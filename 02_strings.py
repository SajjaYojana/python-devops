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

sub_str = sample_str[::-1]
print(sub_str)

