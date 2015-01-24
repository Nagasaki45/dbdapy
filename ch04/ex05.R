# p(language) = .5
# p(language | activated) = ?

# p(language | activated) = p(activated | language) * p(language) / p(activated)

p_language = .5
p_non_language = 1 - p_language
p_activated_g_language = 166 / (166 + 703)
p_activated_g_non_language = 199 / (199 + 2154)
p_activated = p_activated_g_language * p_language +
              p_activated_g_non_language * p_non_language

p_language_g_activated = p_activated_g_language * p_language / p_activated
print(p_language_g_activated)  # 0.6931285
