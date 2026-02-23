-- lua/plugins/colorscheme.lua
return {

  -- Tema principal (recomendo tokyonight-night ou nightfox)
  {
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
    opts = {
      -- Ativa transparência total
      transparent = true,
      -- Estilos transparentes para floats e sidebars
      styles = {
        sidebars = "transparent",
        floats = "transparent",
      },
      -- Tema mais roxo/escuro
      on_colors = function(colors)
        colors.bg = "#0f0e17" -- bem escuro
        colors.bg_dark = "#0a0a12"
        colors.bg_float = "NONE" -- essencial para transparência
        colors.bg_sidebar = "NONE"
        -- Ajuste roxo mais forte se quiser
        -- colors.purple = "#9d7cd8"
        -- colors.magenta = "#bb9af7"
      end,
    },
  },

  -- Configuração global do LazyVim
  {
    "LazyVim/LazyVim",
    opts = {
      -- Define o tema padrão
      colorscheme = "tokyonight-night",
    },
  },

  -- Opcional: força remoção de background em tudo (muito forte)
  {
    "xiyaowong/transparent.nvim",
    lazy = false,
    priority = 999,
    opts = {
      -- grupos que NÃO devem ficar transparentes (se quiser)
      exclude_groups = {
        "CursorLine",
        "StatusLine",
        "StatusLineNC",
      },
    },
    config = function(_, opts)
      require("transparent").setup(opts)
      -- Ativa logo no início
      vim.cmd("TransparentEnable")
    end,
  },
}
