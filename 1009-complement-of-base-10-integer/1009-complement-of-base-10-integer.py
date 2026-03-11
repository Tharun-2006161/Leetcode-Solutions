class Solution:
    def bitwiseComplement(self, n: int) -> int:
        m=(1<<n.bit_length())-1
        return (n^m if n!=0 else 1)