print("Using For :")
for(x in 1:10)
{
    print(x)
}

print("Using while :")
i <- 1
while(i <= 10)
{
    print(i)
    i <- i + 1
}

i <- 1
print("Using repeat :")
repeat
{
    print(i)
    i <- i + 1
    if (i > 10)
    {
        break
    }
}
