{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "wordlist_gen.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMr+pS4NtqRTgDpbJXqB7u2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/junpyo319/RamRaid_colab/blob/main/wordlist_gen_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 169
        },
        "id": "o8tY6wH1BgGr",
        "outputId": "4b29fb88-b3e1-4436-9f52-630ef5ff90f2"
      },
      "source": [
        "import re\n",
        "from itertools import product\n",
        "from google.colab import files\n",
        "\n",
        "header = 'wordlist_gen..'\n",
        "\n",
        "def get_len() :\n",
        "  len_opt = input('set length.. e.g. 4:8..\\t')\n",
        "  return re.split(':',len_opt)\n",
        "\n",
        "def get_chrset() :\n",
        "  chrset_opt1 = input('Do you want to include alphabet into the set? (y/n)\\t')\n",
        "  if chrset_opt1 == 'y' :\n",
        "    chrset_opt1_1 = input('Do you want specify alphabet? (y/n)\\t')\n",
        "    if chrset_opt1_1 == 'y' :\n",
        "      chrset_tmp1 = input('input char set.. e.g. abcd\\t')\n",
        "    elif chrset_opt1_1 == 'n' :\n",
        "      chrset_tmp1 = 'abcdefghijklmnopqrstuvwxyz'\n",
        "    else :\n",
        "      get_chrset()\n",
        "  elif chrset_opt1 == 'n' :\n",
        "    chrset_tmp1 = ''\n",
        "\n",
        "  chrset_opt2 = input('Do you want to include numeric char into the set? (y/n)\\t')\n",
        "  if chrset_opt2 == 'y' :\n",
        "    chrset_opt2_1 = input('Do you want to specify nemeric char?\\t')\n",
        "    if chrset_opt2_1 == 'y' :\n",
        "      chrset_tmp2 = input('input numeric set.. e.g. 1234\\t')\n",
        "    elif chrset_opt2_1 == 'n' :\n",
        "      chrset_tmp2 = '123456789'\n",
        "  elif chrset_opt2 == 'n' :\n",
        "    chrset_tmp2 = ''\n",
        "  else :\n",
        "    get_chrset()\n",
        "\n",
        "  chrset = chrset_tmp1 + chrset_tmp2\n",
        "  print('chrset : ' + chrset)\n",
        "\n",
        "  if not chrset :\n",
        "    print('chrset is empty...')\n",
        "    get_chrset()\n",
        "  elif chrset:\n",
        "    return [chr for chr in chrset]\n",
        "\n",
        "def print_list(len, chrset) :\n",
        "  i = int(len[0])\n",
        "  with open(\"wordlist.txt\", 'w') as f :\n",
        "    for i in range(int(len[0]), int(len[1]) + 1) :\n",
        "      for j in product(chrset, repeat = i) :\n",
        "        wd = ''.join(j)\n",
        "        f.write(wd + '\\n')\n",
        "\n",
        "len = get_len()\n",
        "chrset = get_chrset()\n",
        "print_list(len,chrset)\n",
        "\n",
        "files.download('wordlist.txt')"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "set length.. e.g. 4:8..\t4:4\n",
            "Do you want to include alphabet into the set? (y/n)\ty\n",
            "Do you want specify alphabet? (y/n)\ty\n",
            "input char set.. e.g. abcd\tabcde\n",
            "Do you want to include numeric char into the set? (y/n)\ty\n",
            "Do you want to specify nemeric char?\ty\n",
            "input numeric set.. e.g. 1234\t1234\n",
            "chrset : abcde1234\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "download(\"download_b3f9d69e-043d-4d3a-a25d-761ac7725e13\", \"wordlist.txt\", 32805)"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vfCBfOkuDngH"
      },
      "source": [
        "_"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}