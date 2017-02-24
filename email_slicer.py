
email = input("What is your email id? : ").strip();

at_ret_index = email.index("@")
user_name = email[:at_ret_index]
domain = email[at_ret_index + 1 : ]

output_message = "With {} as your email, you got user name {} and domain {}"
result = output_message.format(email, user_name, domain)
print(result)
