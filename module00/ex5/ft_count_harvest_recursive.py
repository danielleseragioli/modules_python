def ft_count_harvest_recursive():
    last_day = int(input("Days until harvest:"))
    def ft_count_days(i):
        if i <= last_day:
                print(f"Day {i}")
                ft_count_days(i + 1)
        else:
            return 
    ft_count_days(1)

ft_count_harvest_recursive()