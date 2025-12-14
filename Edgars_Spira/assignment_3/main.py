from file_operations import write_message, read_messages

# Application that writes a message to a text file with timestamp and thumbs up emoji
print("Enter a message to write into the file:")
message_input = input()
write_message(message_input)

print("File content:")
print(read_messages())