# SPDX-FileCopyrightText: 2024-present Valerio <svalerio@etudiant.univ-lr.fr>
#
# SPDX-License-Identifier: MIT
def pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
