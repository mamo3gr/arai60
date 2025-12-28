class Solution:
    @staticmethod
    def _get_canonicalized_local_and_domain(email: str) -> tuple[str, str]:
        local_name_raw, _, domain_name = email.rpartition("@")
        if not local_name_raw:
            raise ValueError(f"{email} must have @ and non-empty local name")
        if domain_name[-4:] != ".com":
            raise ValueError(f"{email} must end with .com suffix")
        if len(domain_name) <= 4:
            raise ValueError(
                f"{email} must contain at least one character before .com suffix"
            )

        local_name_without_plus, _, ignored = local_name_raw.partition("+")
        local_name = local_name_without_plus.replace(".", "")
        return local_name, domain_name

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_name_pairs: set[tuple[str, str]] = set()
        for email in emails:
            try:
                local_name, domain_name = self._get_canonicalized_local_and_domain(
                    email
                )
                unique_name_pairs.add((local_name, domain_name))
            except ValueError:
                # ユースケースに合わせてハンドリングする。
                # ここではマーケティング目的でのメール一斉送信を想定し、
                # 失敗したログを落とすことにする（ただしログ出力は省略）
                pass

        return len(unique_name_pairs)
