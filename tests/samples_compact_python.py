SAMPLES_PYTHON = {
    'a': """\
        a1-a: pk
            A1, A2, B1, C1, C2, D1, E1, P1
        """,
    'b': """\
        a1-a: pk
            B1, C1, C2, D1, E1
        a1-b: pk
            B1, C1, C2, D1, E1
        """,
    'c': """\
        a1-a: pk
            C1, C2, D1
        a1-b: pk
            C1, C2, D1
        a1-c: pk
            C1, C2, D1
        """,
    'd': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        """,
    'e': """\
        a1-a: pk
            E1
        a1-b: pk
            E1
        a1-e: pk
            E1
        """,
    'f': """\
        a1-a: pk
            A1, D1
        a1-f: pk a
            F1 None, F2 A1, F3 A1, F4 D1
        """,
    'g': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        a1-g: pk d
            G1 D1
        """,
    'p': """\
        a1-a: pk
            A1, A2, B1, C1, C2, D1, E1, P1
        """,
    'o': """\
        a1-a: pk
            C1, C2, D1
        a1-b: pk
            C1, C2, D1
        a1-c: pk
            C1, C2, D1
        a1-o: pk c s
            O1 None None, O2 C1 None, O3 C2 O1, O4 D1 O3, O5 None O5
        """,
    'm': """\
        a1-m: pk
            M1, M2, M3, M4, M5
        """,
    'm_d': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        a1-m: pk
            M3, M4
        a1-m_d: pk d m
            1 D1 M3, 2 D1 M4
        """,
    'm_s': """\
        a1-m: pk
            M1, M2, M3, M4, M5
        a1-m_s: pk from_m to_m
            1 M2 M1, 2 M1 M2, 3 M4 M3, 4 M3 M4, 5 M5 M3, 6 M3 M5, 7 M5 M4, 8 M4 M5, 9 M5 M5
        """,
    'a_some': """\
        a1-a: pk
            A2, D1
        """,
    'a_some_a_b': """\
        a1-a: pk
            A2, D1
        a1-b: pk
            D1
        """,
    'f_a_d': """\
        a1-a: pk
            A1, D1
        a1-f: pk a
            F1 None, F2 A1, F3 A1, F4 D1
        """,
    'd_a_f': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        a1-f: pk a
            F4 D1
        """,
    'o_one_o_s': """\
        a1-a: pk
            C2, D1
        a1-b: pk
            C2, D1
        a1-c: pk
            C2, D1
        a1-o: pk c s
            O1 None None, O3 C2 O1, O4 D1 O3
        """,
    'm_one_m_s': """\
        a1-m: pk
            M3, M4, M5
        a1-m_s: pk from_m to_m
            3 M4 M3, 4 M3 M4, 5 M5 M3, 6 M3 M5, 7 M5 M4, 8 M4 M5, 9 M5 M5
        """,
    'd_d_m': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        a1-m: pk
            M3, M4
        a1-m_d: pk d m
            1 D1 M3, 2 D1 M4
        """,
    'd_d_m_m_s': """\
        a1-a: pk
            D1
        a1-b: pk
            D1
        a1-c: pk
            D1
        a1-d: pk
            D1
        a1-m: pk
            M3, M4, M5
        a1-m_d: pk d m
            1 D1 M3, 2 D1 M4
        a1-m_s: pk from_m to_m
            3 M4 M3, 4 M3 M4, 5 M5 M3, 6 M3 M5, 7 M5 M4, 8 M4 M5, 9 M5 M5
        """,
}
