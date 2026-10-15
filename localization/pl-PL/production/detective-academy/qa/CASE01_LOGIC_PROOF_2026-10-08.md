# Detective Academy PL — Case 01 logic proof

Date: 2026-10-08
Source: frozen EN V10
Target: `DETECTIVE_ACADEMY_PL_WORKING_MASTER_V1.md`
Case: 01
Status: **PASS / PUZZLE TRUTH PRESERVED**

## Frozen answer

**KNOX at D2**

## Source logic chain

1. QUILL = B1.
2. PIP = row 3.
3. MORSE = column C.
4. All four helpers use distinct rows and distinct columns.
5. PIP is left of QUILL.
6. MORSE is in a lower row than KNOX.

## Polish clue atoms

- `QUILL znajduje się w rzędzie 1, w kolumnie B.`
  - ROW(1)
  - COLUMN(B)
- `PIP znajduje się w rzędzie 3.`
  - ROW(3)
- `MORSE znajduje się w kolumnie C.`
  - COLUMN(C)
- `Każdy pomocnik zajmuje inny rząd i inną kolumnę.`
  - ALL_DIFFERENT_ROWS
  - ALL_DIFFERENT_COLUMNS
- `PIP znajduje się gdzieś na lewo od QUILL.`
  - LEFT_OF(PIP, QUILL)
- `MORSE znajduje się w niższym rzędzie niż KNOX.`
  - LOWER_ROW_THAN(MORSE, KNOX)

No operator was strengthened, weakened or removed.

## Polish solution reconstruction

1. QUILL ma stałą pozycję B1.
2. PIP jest w rzędzie 3, a MORSE w kolumnie C.
3. Każdy pomocnik musi zajmować inny rząd i inną kolumnę.
4. PIP jest na lewo od QUILL. Ponieważ QUILL jest w kolumnie B, a PIP w rzędzie 3, PIP musi zająć A3.
5. Kolumny B, A i C zajmują już QUILL, PIP i MORSE. Dla KNOX zostaje kolumna D.
6. Rzędy 1 i 3 zajmują QUILL i PIP. Dla KNOX i MORSE zostają rzędy 2 i 4.
7. MORSE ma być w niższym rzędzie niż KNOX, więc MORSE = C4, a KNOX = D2.
8. D2 leży w strefie DOSTAWY.

## Result

**KNOX — D2**

The Polish Case 01 clue set preserves the identical single solution.

## Reader-facing solution candidate

**ODPOWIEDŹ: KNOX — D2**

Najpierw ustaw QUILL w B1. PIP musi być w rzędzie 3 i na lewo od QUILL, więc trafia do A3. MORSE zajmuje kolumnę C. Zostaje kolumna D dla KNOX. Rzędy 1 i 3 są już zajęte, więc dla MORSE i KNOX zostają 2 i 4. MORSE ma być niżej niż KNOX, dlatego MORSE trafia do C4, a KNOX do D2. Pole D2 znajduje się w strefie DOSTAWY.

**DLACZEGO TO WAŻNE:** Pierwsza sprawa uczy metody Akademii: najpierw dokładne fakty, potem zależności między tropami, a na końcu eliminacja. Dopiero wtedy wydajesz werdykt.
