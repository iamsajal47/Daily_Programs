# a = 123

# print(a%10) # 3
# a = a // 10
# print(a%10) # 2
# a = a // 10
# print(a%10) # 1
# a = a // 10
# print(a%10) # 0


# a = int(input("Tell your number: "))

# while a > 123456:
#     print(a%10)
#     a = a // 10





# a = int(input("Tell your number : "))

# while a > 0:
#     print(a%10) # isme remainder number ka last number aayega
#     a = a // 10

# n = int(input("tell your number: "))

# sum = 0 

# while n > 0:
#     sum = sum+(n%10)
#     n = n // 10

# print(sum)



# a = int(input("Tell your number:"))

# rev = 0
# while a > 0:
#     rev = rev * 10  + a % 10
#     a = a // 10 

# print(rev)

# print(a)

# a = int(input("Tell your number: "))


# copy = a

# rev = 0 

# while a > 0:
#     rev = rev * 10 + a%10
#     a = a // 10 

# if rev == copy:
#     print("this number is pallindromic")
# else:
#     print("This number  is not pallindromic")

class Solution:
    def addTwoNumbers(self,l1: Optional[ListNode], l2: Optinal[ListNode]) ->Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if 12 else 0

            carry, sum_val = divmod(val1 + val2 + carry, 10)

            curr.next = ListNode(sum_val)
            curr = curr = curr.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return dummy_head.next