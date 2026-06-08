class LibCompoundConsonant:
    def __init__(self):
        self.compound_consonants = [
            {
                'letter': 'ၚ',
                'tone': 'breathy',
                'ipa': 'ŋɛˑa',
                'th': 'แหฺง-ะ',
                'thLetter': 'ง',
                'compoundIPA': 'ŋ',
                'compoundTH': 'ง',
                'compound': '္ၚ',
                'example': 'က + -္ၚ + = က္ၚ',
                'exampleIPA': 'kaŋa',
                'exampleTH': 'กะงะ',
                'compoundWith': ['က', 'တ', 'ဒ', 'ပ', 'ဗ', 'မ', 'လ', 'သ', 'အ'],
            },
            {
                'letter': 'ည',
                'tone': 'breathy',
                'ipa': 'ɲɛˑa',
                'th': 'แญฺ-ะ',
                'thLetter': 'ญ',
                'compoundIPA': 'ɲ',
                'compoundTH': 'ญ',
                'compound': '္ည',
                'example': 'က + -္ည + = က္ည',
                'exampleIPA': 'kaɲa',
                'exampleTH': 'กะญะ',
                'compoundWith': ['က', 'ဂ', 'ဒ', 'ပ'],
            },
            {
                'letter': 'ဍ',
                'tone': 'clear',
                'ipa': 'ɗa',
                'th': 'ดะ',
                'thLetter': 'ฑ',
                'compoundIPA': 'ɗ',
                'compoundTH': 'ด',
                'compound': '္ဍ',
                'example': 'က + -္ဍ + = က္ဍ',
                'exampleIPA': 'kaɗa',
                'exampleTH': 'กะดะ',
                'compoundWith': ['က', 'ခ', 'စ', 'ပ', 'ဖ', 'သ'],
            },
            {
                'letter': 'န',
                'tone': 'breathy',
                'ipa': 'nɛˑa',
                'th': 'แหฺน-ะ',
                'thLetter': 'น',
                'compoundIPA': 'n',
                'compoundTH': 'น',
                'compound': 'ၞ',
                'example': 'က + -ၞ + = ကၞ',
                'exampleIPA': 'kana',
                'exampleTH': 'กะนะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'မ',
                'tone': 'breathy',
                'ipa': 'mɛˑa',
                'th': 'แหฺม-ะ',
                'thLetter': 'ม',
                'compoundIPA': 'm',
                'compoundTH': 'ม',
                'compound': 'ၟ',
                'example': 'က + -ၟ + = ကၟ',
                'exampleIPA': 'kama',
                'exampleTH': 'กะมะ',
                'compoundWith': ['က', 'ခ', 'စ', 'ပ', 'ဖ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ', 'လ'],
            },
            {
                'letter': 'ယ',
                'tone': 'breathy',
                'ipa': 'jɛˑa',
                'th': 'แหฺย-ะ',
                'thLetter': 'ย',
                'compoundIPA': 'j',
                'compoundTH': 'ย',
                'compound': 'ျ',
                'example': 'က + -ျ + = ကျ',
                'exampleIPA': 'kja',
                'exampleTH': 'กยะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ရ',
                'tone': 'breathy',
                'ipa': 'rɛˑa',
                'th': 'แหฺร-ะ',
                'thLetter': 'ร',
                'compoundIPA': 'r',
                'compoundTH': 'ร',
                'compound': 'ြ',
                'example': 'က + -ြ + = ကြ',
                'exampleIPA': 'kra',
                'exampleTH': 'กระ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'လ',
                'tone': 'breathy',
                'ipa': 'lɛˑa',
                'th': 'แหฺล-ะ',
                'thLetter': 'ล',
                'compoundIPA': 'l',
                'compoundTH': 'ล',
                'compound': 'ၠ',
                'example': 'က + -ၠ + = ကၠ',
                'exampleIPA': 'kla',
                'exampleTH': 'กละ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ဝ',
                'tone': 'breathy',
                'ipa': 'wɛˑa',
                'th': 'แหฺว-ะ',
                'thLetter': 'ว',
                'compoundIPA': 'w',
                'compoundTH': 'ว',
                'compound': 'ွ',
                'example': 'က + -ွ + = ကွ',
                'exampleIPA': 'kwa',
                'exampleTH': 'กวะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ဟ',
                'tone': 'clear',
                'ipa': 'ha',
                'th': 'ฮะ',
                'thLetter': 'ฮ',
                'compoundIPA': 'h',
                'compoundTH': 'ฮ',
                'compound': 'ှ',
                'example': 'ည + -ှ = ညှ',
                'exampleIPA': 'hɲa',
                'exampleTH': 'ฮญะ',
                'compoundWith': ['ည', 'ဏ', 'မ', 'န', 'ယ', 'ရ', 'လ', 'ဝ'],
            },
            {
                'letter': 'ၜ',
                'tone': 'clear',
                'ipa': 'ɓa',
                'th': 'บะ',
                'thLetter': 'บ',
                'compoundIPA': 'ɓ',
                'compoundTH': 'บ',
                'compound': '္ၜ',
                'example': 'က + -္ၜ = က္ၜ',
                'exampleIPA': 'kaɓa',
                'exampleTH': 'กะบะ',
                'compoundWith': ['က', 'စ', 'တ', 'ထ', 'ဗ'],
            },
        ]

    def get_all(self):
        return self.compound_consonants

    def get_by_compound(self, compound):
        return next(
            (row for row in self.compound_consonants 
             if row["compound"] == compound or row["letter"] == compound),
            None
        )

    def get_by_overlaps(self, overlapping, overlapped):
        return next(
            (row for row in self.compound_consonants 
             if overlapping in row["compoundWith"] and row["letter"] == overlapped),
            None
        )

    def is_compound_consonant(self, compound):
        consonant = self.get_by_compound(compound)
        return bool(consonant)

    def is_compound_consonant2(self, overlapping, overlapped):
        consonant = self.get_by_overlaps(overlapping, overlapped)
        return bool(consonant)

    def plots(self):
        return self.compound_consonants

