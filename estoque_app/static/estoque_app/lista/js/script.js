// Função para abrir o modal de exclusão e preencher os dados do produto
function openDeleteModal(produtoId, produtoNome) {
  // Atualiza o nome do produto no modal
  document.getElementById("modalProdutoNome").textContent = produtoNome;

  // Atualiza a URL de exclusão no formulário
  const form = document.getElementById("modalForm");
  form.action = `/excluir/${produtoId}/`;
  // Exibe o modal
  document.getElementById("deleteModal").style.display = "block";
}

// Função para fechar o modal de exclusão
function closeModal() {
  document.getElementById("deleteModal").style.display = "none";
}
