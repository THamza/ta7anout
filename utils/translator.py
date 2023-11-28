class Translator:
    """
    A simple translation utility for a Streamlit app.
    """
    def __init__(self):
        self.translations = {
             "English": {
                "title": "Product Sales Dashboard",
                "filter": "Filter Data",
                "average_price": "Average Price",
                "average_margin": "Average Margin",
                "select_sku": "Select SKU",
                "overview_tab": "Overview",
                "analysis_tab": "Detailed Analysis",
                "data_view_tab": "Data View",
                "sales_over_time": "Sales Over Time",
                "margin_analysis": "Margin Analysis",
                "top_selling_products": "Top Selling Products",
                "data_table": "Data Table",
                "download_csv": "Download data as CSV",
                "show_summary": "Show Summary Statistics",
                "upload_prompt": "Drag and Drop or Click to Upload a CSV file",
                "please_upload": "Please upload a CSV file to view the dashboard.",
                "sales_over_sku": "Sales Over SKU",
                "correlation_analysis": "Price-Quantity Correlation",
                "quantity": "Quantity",
                "sku": "SKU",
                "total_sales": "Total Sales",
                "data_error": "The uploaded data is invalid. Please check the file and try again.",
            },
            "Français": {
                "title": "Tableau de Bord des Ventes de Produits",
                "filter": "Filtrer les Données",
                "average_price": "Prix Moyen",
                "average_margin": "Marge Moyenne",
                "select_sku": "Sélectionner le SKU",
                "overview_tab": "Aperçu",
                "analysis_tab": "Analyse Détaillée",
                "data_view_tab": "Vue des Données",
                "sales_over_time": "Ventes au Fil du Temps",
                "margin_analysis": "Analyse de la Marge",
                "top_selling_products": "Produits les Plus Vendus",
                "data_table": "Tableau de Données",
                "download_csv": "Télécharger les données en CSV",
                "show_summary": "Afficher les Statistiques Résumées",
                "upload_prompt": "Faites glisser et déposez ou cliquez pour télécharger un fichier CSV",
                "please_upload": "Veuillez télécharger un fichier CSV pour afficher le tableau de bord.",
                "sales_over_sku": "Ventes par SKU",
                "correlation_analysis": "Corrélation Prix-Quantité",
                "quantity": "Quantité",
                "sku": "SKU",
                "total_sales": "Ventes Totales",
                "data_error": "Les données téléchargées ne sont pas valides. Veuillez vérifier le fichier et réessayer.",
            },
            "العربية": {
                "title": "لوحة مبيعات المنتجات",
                "filter": "تصفية البيانات",
                "average_price": "متوسط السعر",
                "average_margin": "متوسط الهامش",
                "select_sku": "اختر الرقم التسلسلي",
                "overview_tab": "نظرة عامة",
                "analysis_tab": "تحليل مفصل",
                "data_view_tab": "عرض البيانات",
                "sales_over_time": "المبيعات على مر الزمن",
                "margin_analysis": "تحليل الهامش",
                "top_selling_products": "المنتجات الأكثر مبيعا",
                "data_table": "جدول البيانات",
                "download_csv": "تحميل البيانات بصيغة CSV",
                "show_summary": "عرض الإحصائيات الخلاصة",
                "upload_prompt": "قم بسحب وإفلات أو انقر لتحميل ملف CSV",
                "please_upload": "يرجى تحميل ملف CSV لعرض لوحة المعلومات.",
                "sales_over_sku": "المبيعات على مر الزمن",
                "correlation_analysis": "الترابط بين السعر والكمية",
                "quantity": "الكمية",
                "sku": "الرقم التسلسلي",
                "total_sales": "إجمالي المبيعات",
                "data_error": "البيانات التي تم تحميلها غير صالحة. يرجى التحقق من الملف والمحاولة مرة أخرى.",
            },
            "ⵜⴰⵎⴰⵣⵉⵖⵜ": {
                "title": "ⵜⴰⴽⵡⵉⵍⵜ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
                "filter": "ⴰⵣⵔⵣⵉ ⵏ ⵜⵓⵙⴷⴰⵜ",
                "average_price": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⴰⵙⴰⵖⵜ",
                "average_margin": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⴰⴳⴻⵔⵎⵜ",
                "select_sku": "ⴰⴼⴰⵏ ⵏ ⵙⴽⵓ",
                "overview_tab": "ⵜⴰⵏⵎⵉⵔⵜ",
                "analysis_tab": "ⵜⴰⵏⵎⵉⵔⵜ ⵏ ⵜⴰⵎⴰⵡⴰⵙⵜ",
                "data_view_tab": "ⴰⵙⴰⵡⴰⵏ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
                "sales_over_time": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ",
                "margin_analysis": "ⵜⴰⵏⵎⵉⵔⵜ ⵏ ⵜⴰⴳⴻⵔⵎⵜ",
                "top_selling_products": "ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵜⴰⵡⵓⵔⵉ",
                "data_table": "ⵜⴰⴽⵡⵉⵍⵜ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
                "download_csv": "ⴰⵣⴳⴰⵔⵡⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⴳ ⴰⴱⴱⴰⵡⵏ ⵏ ⵙⵉⵙⵡⴰⵖⵜ",
                "show_summary": "ⴰⵙⵏⵓⵔⵓ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ",
                "upload_prompt": "ⵜⴰⴳⴷⵓⴷ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵙⵉⵙⵡⴰⵖⵜ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ", 
                "please_upload": "ⵓⵔⴰ ⵜⵉⵍⵉⵙⵉ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ.",
                "sales_over_sku": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵙⴽⵓ",
                "correlation_analysis": "ⵜⴰⵏⵎⵉⵔⵜ ⵏ ⵜⴰⵙⴰⵖⵜ ⵏ ⵜⴰⴳⴻⵔⵎⵜ",
                "quantity": "ⵜⴰⵙⵉⵏⵏⴰ",
                "sku": "ⵙⴽⵓ",
                "total_sales": "ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⵓⴳⴳⴰⵔⴰ",
                "data_error": "ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⴰⵙⵏⵓⵔⵓ. ⵉⵍⵍⴰ ⵜⴰⵎⵓⵍⵜ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ ⵏ ⵜⵓⴳⴳⴰⵔⴰ ⵏ ⵉⵎⴰⵍⵢⴰⵏ.",
            },
        }

    def get_translation(self, language, key):
        """
        Retrieves a translation based on the specified language and key.

        Parameters:
        - language: The language to translate into.
        - key: The key for the translation term.

        Returns:
        - The translated string if available, otherwise the key itself.
        """
        return self.translations.get(language, {}).get(key, key)

# Usage example
# translator = Translator()
# text = translator.get_translation("Français", "title")
