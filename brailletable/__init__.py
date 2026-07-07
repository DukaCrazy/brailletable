class BrailleTable():
    
#---------------------------------------- Tables group (0004) ----------------------------------------
    #0004-AA
    @staticmethod
    def braille_list() -> list[str]:
        """
        EN
        Returns all braille characters organized in the standard Unicode order, covering the range U+2800 to U+283F.
 
        JP
        Unicode の標準順（U+2800〜U+283F）に従って並べられた点字文字をすべて返します。
        
        IT
        Restituisce tutti i caratteri braille organizzati nell’ordine standard Unicode, coprendo l’intervallo da U+2800 a U+283F.
        
        PT
        Retorna todos os caracteres braille organizados na ordem padrão do Unicode, cobrindo o intervalo de U+2800 a U+283F.
        
        CH
        返回按 Unicode 标准顺序排列的所有点字符号，范围覆盖 U+2800 至 U+283F。
        """
        return [
            '⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇',
            '⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏',
            '⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗',
            '⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟',
            '⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧',
            '⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯',
            '⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷',
            '⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿'
        ]
    
    #0004-AB
    @staticmethod
    def reverse_braille_list() -> list[str]:
        """
        EN
        Returns all 64-dot Braille characters organized in reverse binary order (mirrored bit mapping), ideal for fast decoding and indexing.

        JP
        高速なデコードやインデックス作成に適した、逆バイナリ順（反転ビットマッピング）で並べられた6点点字の全64文字を返します。

        IT
        Restituisce tutti i 64 caratteri braille a 6 punti organizzati in ordine binario inverso (mappatura dei bit speculare), ideale per la decodifica rapida e l'indicizzazione.

        PT
        Retorna todos os 64 caracteres braille de 6 pontos organizados na ordem binária inversa (mapeamento de bits espelhado), ideal para decodificação rápida e indexação.

        CH
        返回按逆二进制顺序（镜像位映射）排列 All 64 个六点点字符号，非常适合快速解码和索引。
        """
        return [
            '⠀','⠈','⠐','⠘','⠠','⠨','⠰','⠸',
            '⠁','⠉','⠑','⠙','⠡','⠩','⠱','⠹',
            '⠂','⠊','⠒','⠚','⠢','⠪','⠲','⠺',
            '⠃','⠋','⠓','⠛','⠣','⠫','⠳','⠻',
            '⠄','⠌','⠔','⠜','⠤','⠬','⠴','⠼',
            '⠅','⠍','⠕','⠝','⠥','⠭','⠵','⠽',
            '⠆','⠎','⠖','⠞','⠦','⠮','⠶','⠾',
            '⠇','⠏','⠗','⠟','⠧','⠯','⠷','⠿'
        ]
    
    #0004-BA
    @staticmethod
    def binary_list() -> list[list[int]]:
        """
        EN
        Returns a list with 64 items; each item is an array of 6 bits representing a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字を表す 6 ビットの配列です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array di 6 bit che rappresenta un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é um array de 6 bits que representa um caractere braille.

        CH
        返回一个包含 64 个项目的列表；每个项目都是由 6 位组成的数组，用于表示一个点字符号。
        """
        result = []

        for number in range(64):

            binary_text = format(number, "06b")

            bits = []
            for char in binary_text:
                bits.append(int(char))

            result.append(bits)

        return result
    
    #0004-BB
    @staticmethod
    def reverse_binary_list() -> list[list[int]]:
        """
        EN
        Returns a list with 64 items; each item is an array of 6 bits representing a braille character,
        but with the bit order reversed (e.g., 000001 becomes 100000).

        JP
        64 個の項目を持つリストを返します。各項目は点字文字を表す 6 ビットの配列ですが、
        ビットの並び順が反転しています（例: 000001 → 100000）。

        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array di 6 bit che rappresenta un carattere braille,
        ma con l’ordine dei bit invertito (ad esempio: 000001 → 100000).

        PT
        Retorna uma lista com 64 itens; cada item é um array de 6 bits que representa um caractere braille,
        porém com a ordem dos bits invertida (ex.: 000001 → 100000).

        CH
        返回一个包含 64 个项目的列表；每个项目都是由 6 位组成的数组，用于表示一个点字符号，
        但位顺序已反转（例如：000001 → 100000）。
        """
        result = []

        for number in range(64):

            binary_text = format(number, "06b")

            bits = []
            for char in reversed(binary_text):
                bits.append(int(char))

            result.append(bits)

        return result

    #0004-CA
    @staticmethod
    def binary_string_list() -> list[str]:

        result = []

        for number in range(64):

            binary_text = format(number, "06b")

            result.append(binary_text)

        return result
    
    #0004-CB
    @staticmethod
    def reverse_binary_string_list() -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is a 6‑bit binary string representing a braille character,
        but with the bit order reversed (e.g., 000001 becomes 100000).

        JP
        64 個の項目を持つリストを返します。各項目は点字文字を表す 6 ビットの文字列ですが、
        ビットの並び順が反転しています（例: 000001 → 100000）。

        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa binaria di 6 bit che rappresenta un carattere braille,
        ma con l’ordine dei bit invertito (ad esempio: 000001 → 100000).

        PT
        Retorna uma lista com 64 itens; cada item é uma string binária de 6 bits que representa um caractere braille,
        porém com a ordem dos bits invertida (ex.: 000001 → 100000).

        CH
        返回一个包含 64 个项目的列表；每个项目都是一个由 6 位组成的二进制字符串，用于表示一个点字符号，
        但位顺序已反转（例如：000001 → 100000）。
        """
        result = []

        for number in range(64):

            binary_text = format(number, "06b")   # ex.: "000001"

            reversed_text = ""
            for char in reversed(binary_text):
                reversed_text += char             # ex.: "100000"

            result.append(reversed_text)

        return result
    
    #0004-D
    @staticmethod
    def unicode_list() -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is the Unicode code in hexadecimal format corresponding to a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字に対応する Unicode の 16 進コードです。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è il codice Unicode in formato esadecimale corrispondente a un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é o código Unicode em formato hexadecimal correspondente a um caractere braille.

        CH
        返回一个包含 64 个项目的列表；每个项目都是对应点字符号的 Unicode 十六进制代码。
        """
        return [f"{0x2800 + i:04x}" for i in range(64)]
    
    #0004-E
    @staticmethod
    def dot_count() -> list[int]:
        """
        EN
        Returns a list with 64 items; each item is an integer indicating how many points are active (1 to 6) in the corresponding braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の数を示す整数です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un intero che indica quanti punti (da 1 a 6) sono attivi nel carattere braille corrispondente.
        PT
        Retorna uma lista com 64 itens; cada item é um inteiro indicando quantos pontos estão ativos (1 a 6) no caractere braille correspondente.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个整数，用于表示对应点字符号中有多少个激活点（1 至 6）。
        """
        return [bin(i).count("1") for i in range(64)]
    
    #0004-F
    @staticmethod
    def dot_numbering_list() -> list[list[int]]:
        """
        EN
        Returns a list with 64 items; each item is an array containing the numbers of the active points (1 to 6) of the corresponding braille character. Commonly used in educational materials.
        
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号を含む配列です。教育用資料でよく使用されます。
        
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente. Molto utilizzato in materiali didattici.
        
        PT
        Retorna uma lista com 64 itens; cada item é um array contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente. Muito usado em materiais didáticos.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个数组，包含对应点字符号中激活点（1 至 6）的编号。常用于教学材料。
        """
        lst = []
        for i in range(64):
            dots = []
            for d in range(6):
                if (i >> d) & 1:
                    dots.append(d+1)
            lst.append(dots)
        return lst
    
    #0004-G
    @staticmethod
    def dot_numbering_string_list() -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is a string containing the numbers of the active points (1 to 6) of the corresponding braille character, separated by hyphens. Commonly used in educational materials.
        
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号をハイフンで区切った文字列です。教育用資料でよく使用されます。
        
        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente, separati da trattini. Molto utilizzato in materiali didattici.
        
        PT
        Retorna uma lista com 64 itens; cada item é uma string contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente, separados por hífens. Muito usado em materiais didáticos.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个字符串，包含对应点字符号中激活点（1 至 6）的编号，并以连字符分隔。常用于教学材料。
        """
        return [
            "-".join(str(d) for d in dots)
            for dots in BrailleTable.dot_numbering_list()
        ]
    
#---------------------------------------- Mapping group (0003) ----------------------------------------
    #0003-AA
    @staticmethod
    def get_braille_to_index(braille: str) -> int:
        """
        EN
        Receives a character (string), which must be a valid braille symbol, 
        and returns an integer (int) that represents its position in the Unicode braille table (U+2800 to U+283F).
        
        JP
        1 文字の入力（string）を受け取り、その文字が有効な点字記号であることを前提として、
        Unicode の点字表（U+2800～U+283F）における位置を表す整数（int）を返します。

        IT
        Riceve un carattere (stringa), che deve essere un simbolo braille valido, 
        e restituisce un intero (int) che rappresenta la posizione corrispondente nella tabella Unicode del braille (U+2800–U+283F).
        
        PT
        Recebe um caractere (string), obrigatoriamente correspondente a um símbolo braille, 
        e retorna um inteiro (int) que representa a posição na tabela Unicode do braille (U+2800 a U+283F).

        CH
        接收一个字符（string），该字符必须是有效的点字符号，并返回一个整数（int），表示其在 Unicode 点字表（U+2800 至 U+283F）中的位置。
        """
        braille_to_index = {
        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63
    }
        return braille_to_index[braille]
    #0003-AB
    @staticmethod
    def get_index_to_braille(index: int) -> str:
        braille_list = [
            '⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇',
            '⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏',
            '⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗',
            '⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟',
            '⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧',
            '⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯',
            '⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷',
            '⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿'
        ]
        return braille_list[index]
        
    #0003-B
    @staticmethod
    def get_braille_list_to_index_list(braille_list: list[str]) -> list[int]:
        """
        EN
        Receives multiple characters (strings), each of which must be a valid braille symbol, and returns a list of integers (int), 
        where each value represents the position of the corresponding symbol in the Unicode braille table (U+2800 to U+283F).

        JP
        複数の文字（string）を受け取り、各文字が有効な点字記号であることを前提として、
        Unicode の点字表（U+2800～U+283F）における各記号の位置を表す整数（int）のリストを返します。

        IT
        Riceve più caratteri (stringhe), ognuno dei quali deve essere un simbolo braille valido, e restituisce una lista di interi (int), 
        in cui ogni valore rappresenta la posizione del rispettivo simbolo nella tabella Unicode del braille (U+2800–U+283F).
        
        PT
        Recebe múltiplos caracteres (string), cada um obrigatoriamente correspondente a um símbolo braille,
        e retorna uma lista de inteiros (int), onde cada valor representa a posição do respectivo símbolo
        na tabela Unicode do braille (U+2800 a U+283F).

        CH
        接收多个字符（string），每个字符都必须是有效的点字符号，并返回一个整数（int）列表，其中每个值表示相应符号在 Unicode 点字表（U+2800 至 U+283F）中的位置。
        """
        return [BrailleTable.get_braille_to_index(b) for b in braille_list]
