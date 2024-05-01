<h1 align="center">Tokenization Tutorial</h1>

<p align="center">
  <h1 align="center">
    UNIX Commands
  </h1>
  <p><code>cat ja_pud-ud-test.conllu | grep -v "^#" | cut -f2 | python3 japan-originaltxt.py</code></p>
  <p>Get original text: Look at 2nd tab of lines starting with "#." Code splits into 3 files: full text, first 80% text, last 20% text</p>

  <p><code>cat ja_pud-ud-test.conllu | grep -v "^#" | cut -f2 | python3 japan-tokentxt.py</code></p>
  <p>Get tokenized text: Look at 2nd tab of lines starting with "#." Code splits into 3 files: full text, first 80% text, last 20% text</p>

  <p><code>cat ja_pud-ud-test.conllu | grep -v "^#" | cut -f2 | python3 japan-make-dict.py</code></p>
  <p>Get Dictionary</p>

  <p><code>cat original.test.txt | python3 maxmatch.py dictionary.txt > output.test.txt</code></p>
  <p">Run maxmatch using test data and dictionary</p>

  <p><code>python3 evaluate.py output.test.txt tokenized.test.txt</code></p>
  <p>Evaluate Word Error Rate</p>

  <h1 align="center">Performance & Findings</h1>
  <p>The word error rate for this program is 6.45%. One example of incorrect tokenization are the tokens な る being grouped as one, individual token. Additionally, the program cannot output a desired EVA value.
</p>