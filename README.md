# BFuzz

```
BFuzz is currently in beta. 
Note: Fuzzing Chrome in BFuzz is still in process
```

BFuzz is an input based browser fuzzer tool which take `.html` & `.xml` as an input, open's up your browser with a new instance and pass multiple testcases which is present in `recurve` folder of BFuzz, we can simply keep adding testcases in `recurve`

## Run BFuzz

```
warmachine@ftw:~/BFuzz$ python BFuzz.py 
Enter the browser type:  
 1: Chrome 
 2: Firefox
>>
```
Running `python BFuzz.py` will ask for option for now select `2` this will open firefox `firefox --new-instance` and randomly open any of the testcase from `recurve` create the logs on the terminal wait for `3 seconds` again it will open `firefox` and the process continue so on.

BFuzz is a small `.py` script which enable's to open browser run testcase for `12 seconds` the close wait for `3 seconds` and again follow the same process.

The testcase's in `recurve` is been collected by different `exploit DB` forums a huge ShouOut to respective security researcher's to wrote such tescases, most of the testcase are from `Google Project Zero`

## BFuzz On Action

Here is one of the example which running BFuzz on `Epiphany Web 3.28.1`: Bug ID: GNOME, 95740 
However a `Stack Overflow` was also observed while running `BFuzz` on Firefox but it went duplicate, FF Bug ID: `1456083`
Video: https://youtu.be/I59SkL0ReUM

## Contribution

Please feel free to PR.

## ToDo

Handle Exeception, Add banner, Add more testcases, Optimize Code.
