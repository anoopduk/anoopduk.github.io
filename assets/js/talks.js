(() => {
  const list = document.getElementById("engagement-list");
  const search = document.getElementById("engagement-search");
  const year = document.getElementById("engagement-year");
  const clear = document.getElementById("engagement-clear");
  const count = document.getElementById("engagement-count");

  if (!list || !search || !year || !clear || !count) return;

  const items = Array.from(list.querySelectorAll("li[data-year]"));
  const years = [...new Set(items.map((item) => item.dataset.year))].sort(
    (a, b) => Number(b) - Number(a),
  );

  years.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    year.appendChild(option);
  });

  const normalise = (value) =>
    String(value || "")
      .toLocaleLowerCase("en")
      .replace(/\s+/g, " ")
      .trim();

  const apply = () => {
    const query = normalise(search.value);
    const selectedYear = year.value;
    let visible = 0;

    items.forEach((item) => {
      const matchesText = !query || normalise(item.textContent).includes(query);
      const matchesYear = !selectedYear || item.dataset.year === selectedYear;
      item.hidden = !(matchesText && matchesYear);
      if (!item.hidden) visible += 1;
    });

    count.textContent =
      visible === items.length
        ? `${visible} engagements`
        : `${visible} of ${items.length} engagements`;
  };

  search.addEventListener("input", apply);
  year.addEventListener("change", apply);
  clear.addEventListener("click", () => {
    search.value = "";
    year.value = "";
    apply();
    search.focus();
  });
  search.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      search.value = "";
      apply();
    }
  });

  apply();
})();
