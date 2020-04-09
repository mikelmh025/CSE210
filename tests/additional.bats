load harness

@test "additional-1" {
  check '2 + 3 - 4' '1'
}


@test "additional-2" {
  check '-2 - 3 * -4 ^ 6 * 2 * 0' '-2'
}


@test "additional-3" {
  check '2 - 3 - 4 ^ 6' '-4097'
}


@test "additional-4" {
  check '2 + -3 ^ 4' '83'
}


@test "additional-5" {
  check '2 * 3 ^ 4' '162'
}


@test "additional-6" {
  check '2 * 3 ^ 4 + 7 - 6 * -8' '217'
}
