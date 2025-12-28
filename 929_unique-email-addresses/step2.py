class Solution:
    @staticmethod
    def _get_local_and_domain(email: str) -> tuple[str, str]:
        local_name, domain_name, *rest = email.split("@")
        if rest:
            raise ValueError(f"There are two or more @ in {email}")

        local_name_normalized = local_name.replace(".", "").split("+")[0]
        return local_name_normalized, domain_name

    @staticmethod
    def _get_local_and_domain_naive(email: str) -> tuple[str, str]:
        """
        emailを走査するのは一度だけにした実装。こちらの方が理論上速そうだが、
        str.split() や .replace() の方がネイティブ実行なので実際速いみたい。
        可読性も拡張性も低そう
        """
        local_chars = []
        i = 0
        while i < len(email):
            c = email[i]

            if c == ".":
                i += 1
                continue

            if c == "+":
                while i < len(email) and email[i] != "@":
                    i += 1
                break

            if c == "@":
                break

            local_chars.append(c)
            i += 1

        local_name = "".join(local_chars)
        domain_name = email[i + 1 :]
        return local_name, domain_name

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            unique_emails.add(self._get_local_and_domain(email))

        return len(unique_emails)
