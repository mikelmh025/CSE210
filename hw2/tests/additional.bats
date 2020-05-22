load harness

@test "additional-1" {
  check 'if x <= 2 ∧ x >= 1 then y := 1 else z := 1' '{z → 1}'
}

@test "additional-2" {
  check 'x := 1 if x <= 2 then skip else x := x + 1' '{}'
}

@test "additional-3" {
  check 'if x >= 0 then x := 1 else x := 0' '{x → 1}'
}

@test "additional-4" {
  check 'while x <= 1 do x := 3' '{x → 3}'
}

@test "additional-5" {
  check 'while x >= 0 do x := x - 3' '{x → -3}'
}

