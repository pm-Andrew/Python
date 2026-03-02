# Just setting up my twttr

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">just setting up my twttr</p>&mdash; jack⚡️ (@jack) <a href="https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw">March 21, 2006</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called *twttr*. In a file called `twttr.py`, implement a program that prompts the user for a `str` of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

{% spoiler Hints %}
* Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.
* Much like a `list`, a `str` is "iterable," which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:
  ```py
  for c in s:
      print(c, end="")
  ```
{% endspoiler %}

## Demo

<script async data-autoplay="1" data-cols="80" data-loop="1" data-rows="12" id="asciicast-Nv6iLIjNIdxofiRExZ5K9mBHS" src="https://asc
iinema.org/a/Nv6iLIjNIdxofiRExZ5K9mBHS.js"></script>

## Before You Begin

Log into <https://code.cs50.io/>, click on your terminal window, and execute `cd` by itself. You should find that your terminal window's prompt resembles the below:

```
$
```

Next execute

```
mkdir twttr
```

to make a folder called `twttr` in your codespace.

Then execute

```
cd twttr
```

to change directories into that folder. You should now see your terminal prompt as `twttr/ $`. You can now execute

```
code twttr.py
```

to make a file called `twttr.py` where you'll write your program.

## How to Test

Here's how to test your code manually:

* Run your program with `python twttr.py`. Type `Twitter` and press Enter. Your program should output:
  ```
  Twttr   
  ```
* Run your program with `python twttr.py`. Type `What's your name?` and press Enter. Your program should output: 
  ```
  Wht's yr nm?
  ```
* Run your program with `python twttr.py`. Type `CS50` and press Enter. Your program should output
  ```
  CS50
  ```

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/twttr
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/twttr
```
