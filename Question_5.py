def tower_of_hanoi(num_disks):
    if num_disks <= 0:
        return
    
    total_moves = 2**num_disks - 1
    
    
    if num_disks % 2 == 1:
        source_peg, auxiliary_peg, target_peg = "A", "B", "C"
    else:
        source_peg, auxiliary_peg, target_peg = "A", "C", "B"
    
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            print(f"Move disk 1 from {source_peg} to {target_peg}")
        elif i % 3 == 2:
            print(f"Move disk 2 from {source_peg} to {auxiliary_peg}")
        elif i % 3 == 0:
            print(f"Move disk 1 from {target_peg} to {auxiliary_peg}")
        
        
        if i % 2 == 1:
            source_peg, auxiliary_peg, target_peg = source_peg, target_peg, auxiliary_peg
        else:
            source_peg, auxiliary_peg, target_peg = source_peg, auxiliary_peg, target_peg


num_disks = int(input("Enter the number of disks: "))


tower_of_hanoi(num_disks)


