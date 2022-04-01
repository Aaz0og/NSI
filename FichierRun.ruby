'''
Make a calculator that can add, subtract, multiply and divide
'''

def add(x, y)
  return x + y
end

def subtract(x, y)
  return x - y
end

def multiply(x, y)
  return x * y
end

def divide(x, y)
  return x / y
end

def prompt(string)
  puts "=> #{string}"
end

prompt "Welcome to Calculator! Enter your name"

name = ''
loop do
  name = gets.chomp
  if name.empty?
    prompt "Make sure to use a valid name"
  else
    break
  end
end

prompt "Hi #{name}!"

loop do # main loop
  number1 = ''
  loop do
    prompt "What's the first number?"
    number1 = gets.chomp

    if number1.empty? || number1.to_f <= 0
      prompt "Make sure to use a valid number"
    else
      break
    end
  end

  number2 = ''
  loop do
    prompt "What's the second number?"
    number2 = gets.chomp

    if number2.empty? || number2.to_f <= 0
      prompt "Make sure to use a valid number"
    else
      break
    end
  end

  operator_prompt = <<-MSG
    What operation would you like to perform?
    1) add
    2) subtract
    3) multiply
    4) divide
  MSG

  prompt operator_prompt

  operator = ''
  loop do
    operator = gets.chomp

    if %w(1 2 3 4).include?(operator)
      break
    else
      prompt "Must choose 1, 2, 3, or 4"
    end
  end
end
