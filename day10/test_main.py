from main import auto_completion_score, calc_part_b_score

sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

def test_auto_completion_score():
    assert 288957 == auto_completion_score('[({(<(())[]>[[{[]{<()<>>')
    assert 5566 == auto_completion_score('[(()[<>])]({[<{<<[]>>(')
    assert 1480781 == auto_completion_score('(((({<>}<{<{<>}{[]{[]{}')
    assert 995444 == auto_completion_score('{<[[]]>}<{[{[{[]{()[[[]')
    assert 294 == auto_completion_score('<{([{{}}[<[[[<>{}]]]>[]]')

def test_part_b_score():
    assert 288957 == calc_part_b_score(sample_input)
