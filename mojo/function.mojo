# def function

def greet(name):
    greeting = "Hello, " + name + "!"
    return greeting

def greet2(name: String) -> String:
    var greeting = "Hello, " + name + "!"
    return greeting

fn greet3(name: String) -> String:
    var greeting = "Hello, " + name + "!"
    return greeting

fn pow(base: Int, exp: Int = 2) -> Int:
    return base ** exp

fn use_defaults():
    # Uses the default value for `exp`
    var z = pow(3)
    print(z)

fn use_keywords():
    # Uses keyword argument names (with order reversed)
    var z = pow(exp=3, base=2)
    print(z)

# Variadic arguments

fn sum(*values: Int) -> Int:
  var sum: Int = 0
  for value in values:
    sum = sum+value
  return sum

fn make_worldly(inout *strs: String):
    # Requires extra [] to dereference the reference for now.
    for i in strs:
        i[] += " world"

fn make_worldly2(inout *strs: String):
    # This "just works" as you'd expect!
    for i in range(len(strs)):
        strs[i] += " world"

# Positional-only arguments

fn min(a: Int, b: Int, /) -> Int:
    return a if a < b else b
    # only can call using min(1, 2)

# Keyword-only arguments

fn kw_only_args(a1: Int, a2: Int, *, double: Bool) -> Int:
    var product = a1 * a2
    if double:
        return product * 2
    else:
        return product
    # only can call using kw_only_args(1, 2, double=True)

# Overloaded functions

fn add(x: Int, y: Int) -> Int:
    return x + y

fn add(x: String, y: String) -> String:
    return x + y

@value
struct MyString:
    fn __init__(inout self, string: StringLiteral):
        pass
 
fn foo(name: String):
    print("String")

fn foo(name: MyString):
    print("MyString")

fn call_foo():
    var string = "Hello"
    # foo(string) # This call is ambiguous because two `foo` functions match it
    foo(MyString(string))