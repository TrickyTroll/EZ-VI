#######################################################################
#                       Character Encoding                            #
#######################################################################

def ez_encode_str(to_encode: str) -> list:
    """ Encodes a `str` per character and puts them into a list.

    :type to_encode: str
    :param to_encode: The string that has to be encoded.

    :rtype: list
    :return: A list of encoded chars. Encodes in UTF-8
    """
    to_return = []
    for char in list(to_encode):
        if type(char) != bytes:
            try:
                to_return.append(char.encode("utf-8"))
            except AttributeError:
                raise Exception("`to_encode` must be of type `str`")
        else:
            # This is a problem as they could be encoded differently.
            to_return.append(char)
    return to_return


#######################################################################
#                            Vi tools                                 #
#######################################################################


# Writing

def write_chars(to_write) -> list:
    """To type ``to_write`` to the file.

    ``write_chars`` will type the passed string after the cursor position. 
    From Vi’s command mode, it types ``a`` to insert after and then types the 
    string.

    Usage:

    `In a config file:`

    .. code-block:: yaml

      - write_chars: "snake"

    `Using the API:`

    .. code-block:: python

      ezvi.tools.write_chars("snek")

    :type to_write: str
    :param to_write: The characters to write.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    to_write = "a" + to_write + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


def write_line(to_write):
    """To type `to_write` and create a new line.

    Starts typing after the current cursor position by pressing
    ``a`` from the command mode. ``to_write`` is then typed and
    a new line is created. 

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -write_line("Python is fun.")

    `Using the API:`

    .. code-block:: python

      ezvi.tools.write_line("Python is fun.")

    :type to_write: str
    :param to_write: The characters to write.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    to_write = "a" + to_write + "\n" + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


def new_line(amount):
    """Creates an ``amount`` of new lines.

    ``new_line`` inserts a certain amount of new lines to the file. 
    From Vi’s command mode, ``ezvi`` first presses ``o``. This ensures 
    that the current line won’t be split even if the cursor is not 
    at the end of the line.

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -new_line(3)


    `Using the API:`

    .. code-block:: python

      ezvi.tools.new_line(3)

    :type amount: int
    :param amount: The amount of new lines to create.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    if type(amount) != int:
        try:
            amount = int(amount)
        except TypeError:
            amount = 1

    to_write = "o" + "\n" * (amount-1) + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


def new_line_over():
    """Creates a new line over the cursor.

    The cursor is also moved to the begining of the new line. It is
    not possible to create more than one new line over the cursor
    at a time for now.

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -new_line_over()


    `Using the API:`

    .. code-block:: python

      ezvi.tools.new_line_over()

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    to_write = "O" + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


def write_after_word(to_write):
    """To write ``to_write`` after the current word.

    This function uses ``e`` from the command mode to go to the end
    of the word. ``to_write`` is then written after the end of the
    word using the ``a`` command. **This function does not add a
    space to the begining of ``to_write``.**

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -write_after_word(" General Kenobi.")

    `Using the API:`

    .. code-block:: python

      ezvi.tools.write_after_word(" General Kenobi.")

    :type to_write: str
    :param to_write: What to write after the word.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    prepend = "e" + "a"
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


def write_after_line(to_write):
    """To write ``to_write`` after the current line.

    This function uses ``$`` from the command mode to go to the 
    end of the line. ``to_write`` is then written after the cursor
    position using the ``a`` command. **This function does not add a
    space to the begining of ``to_write``.**

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -write_after_line(" General Kenobi.")

    `Using the API:`

    .. code-block:: python

      ezvi.tools.write_after_line(" General Kenobi.")

    :type to_write: str
    :param to_write: What to write after the line.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    prepend = "$" + "a"
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


def write_after_char(to_write):
    """To write ``to_write`` after the cursor's position (current char).

    ``to_write`` is written after the cursor
    position using the ``a`` command. 

    Usage:

    `In a config file:`

    .. code-block:: yaml

      -write_after_char("Greetings!")

    `Using the API:`

    .. code-block:: python

      ezvi.tools.write_after_char("Greetings!")

    :type to_write: str
    :param to_write: What to write after the cursor.

    :rtype: list
    :return: A list of encoded characters that can be directly interpreted by ``Vi``.
    """

    prepend = "a"
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


def write_before_word(to_write):
    """To type `to_write` before `thing`. `thing` could be line, word or char.

    :rtype: list
    """

    prepend = "b" + "a"  # TODO: Replace "b" by something that works.
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


def write_before_line(to_write):
    """To type `to_write` at the end of the line.

    :rtype: list
    """

    prepend = "0" + "i"
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


def write_before_char(to_write):
    """To type `to_write` before the cursor's position.

    :rtype: list
    """

    prepend = "i"
    append = chr(27)
    to_write = prepend + to_write + append
    to_write = ez_encode_str(to_write)

    return to_write


# Movement

def goto_line(line_num):
    """To move the cursor to `line_num`.

    :rtype: list
    """

    to_write = str(line_num) + "G"
    to_write = ez_encode_str(to_write)

    return to_write


def goto_column(column_num):
    """To move the cursor to `column_num` on the current line.

    :rtype: list
    """

    # This would be much cleaner if I could get the cursor's position.
    to_write = "0" + str(column_num - 1) + "l"
    to_write = ez_encode_str(to_write)

    return to_write


# Replace functions

def replace(start, end, new):
    """To replace from `start` to `end` on the current line.

    :rtype: list
    """

    movement = goto_column(start)
    replace = "c" + str(end - start)
    to_write = movement + replace + new + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


def find_replace(old, new):
    """To find `old` on the current line and replaces it with `new`."""

    pass


def replace_line(new):
    """To replace the whole line with `new`.

    :rtype: list
    """

    movement = "0"
    replace = "c" + "$"
    to_write = movement + replace + new + chr(27)
    to_write = ez_encode_str(to_write)

    return to_write


# Vi commands

def write_file(filename):
    """To write the contents to `filename`.

    :rtype: list
    """

    to_write = ":w " + filename + "\n"
    to_write = ez_encode_str(to_write)

    return to_write


def quit_editor():
    """To quit the editor.

    :rtype: list
    """

    to_write = ":q" + "\n"
    to_write = ez_encode_str(to_write)

    return to_write


def force_quit_editor():
    """To force quit the editor.

    :rtype: list
    """

    to_write = ":q!" + "\n"
    to_write = ez_encode_str(to_write)

    return to_write


all_tools = {
    write_chars.__name__: write_chars,
    write_line.__name__: write_line,
    new_line.__name__: new_line,
    new_line_over.__name__: new_line_over,
    write_after_word.__name__: write_after_word,
    write_after_line.__name__: write_after_line,
    write_after_char.__name__: write_after_char,
    write_before_word.__name__: write_before_word,
    write_before_line.__name__: write_before_line,
    write_before_char.__name__: write_before_char,
    goto_line.__name__: goto_line,
    goto_column.__name__: goto_column,
    replace.__name__: replace,
    replace_line.__name__: replace_line,
    write_file.__name__: write_file,
    quit_editor.__name__: quit_editor,
    force_quit_editor.__name__: force_quit_editor,
}
