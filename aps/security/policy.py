class PolicyEngine:
    def allows(self, permissions, permission): return '*' in permissions or permission in permissions
