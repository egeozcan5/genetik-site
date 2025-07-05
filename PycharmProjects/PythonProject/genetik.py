import streamlit as st
dil = st.sidebar.selectbox(
    "Dil Seçin / Select Language",
    ["Türkçe", "English"]
)
st.sidebar.title("Genetik Bilgi Rehberi" if dil == "Türkçe" else "Genetic Information Guide")
kategori = st.sidebar.selectbox(
    "Bir hastalık kategorisi seçin:" if dil == "Türkçe" else "Select a disease category:",
    [
        "Kategori Seçin" if dil == "Türkçe" else "Select Category",
        "Kanser" if dil == "Türkçe" else "Cancer",
        "Nörolojik Hastalıklar" if dil == "Türkçe" else "Neurological Diseases",
        "Kalıtsal Metabolik Hastalıklar" if dil == "Türkçe" else "Hereditary Metabolic Diseases",
        "Psikolojik Hastalıklar" if dil == "Türkçe" else "Psychiatric Disorders"
    ]
)
if kategori == ("Kategori Seçin" if dil == "Türkçe" else "Select Category"):
    st.title("Genetik Bilgi Rehberi'ne Hoş Geldiniz!" if dil == "Türkçe" else "Welcome to the Genetic Information Guide!")
    st.write("Sol menüden bir hastalık seçerek başlayabilirsiniz." if dil == "Türkçe" else "Start by selecting a disease from the sidebar.")
elif kategori == ("Kanser" if dil == "Türkçe" else "Cancer"):
    kansertut = st.sidebar.selectbox(
        "Bir kanser türü seçin" if dil == "Türkçe" else "Select a cancer type",
        [
            "Seçim Yapın" if dil == "Türkçe" else "Select",
            "Göğüs Kanseri" if dil == "Türkçe" else "Breast Cancer",
            "Yumurtalık Kanseri" if dil == "Türkçe" else "Ovarian Cancer",
            "Prostat Kanseri" if dil == "Türkçe" else "Prostate Cancer",
            "Kolorektal Kanser" if dil == "Türkçe" else "Colorectal Cancer",
            "Akciğer Kanseri" if dil == "Türkçe" else "Lung Cancer",
            "Pankreas Kanseri" if dil == "Türkçe" else "Pancreatic Cancer"
        ]
    )
    if kansertut == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
        st.header("Kanser" if dil == "Türkçe" else "Cancer")
        st.write("Kanser hakkında bilgiler" if dil == "Türkçe" else "Information about cancer")
        st.sidebar.write("Bir kanser türü seçerek o tür hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a cancer type to get information about it.")
    elif kansertut == ("Göğüs Kanseri" if dil == "Türkçe" else "Breast Cancer"):
        gen = st.sidebar.selectbox(
            "Göğüs Kanseri ile ilgili genler" if dil == "Türkçe" else "Breast Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "BRCA1", "BRCA2", "TP53", "HER2"]
        )
        if gen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Göğüs Kanseri" if dil == "Türkçe" else "Breast Cancer")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak genler hakkında detaylı bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view detailed information.")
        elif gen == "BRCA1":
            st.header("BRCA1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "BRCA2":
            st.header("BRCA2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "TP53":
            st.header("TP53")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "HER2":
            st.header("HER2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif kansertut == ("Yumurtalık Kanseri" if dil == "Türkçe" else "Ovarian Cancer"):
        gen = st.sidebar.selectbox(
            "Yumurtalık Kanseri ile ilgili genler" if dil == "Türkçe" else "Ovarian Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "BRCA1", "BRCA2", "RAD51C", "RAD51D"]
        )
        if gen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Yumurtalık Kanseri" if dil == "Türkçe" else "Ovarian Cancer")
            st.write("Bilgi." if dil == "Türkçe" else "Information.")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak genler hakkında detaylı bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view detailed information.")
        elif gen == "BRCA1":
            st.header("BRCA1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "BRCA2":
            st.header("BRCA2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "RAD51C":
            st.header("RAD51C")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "RAD51D":
            st.header("RAD51D")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif kansertut == ("Prostat Kanseri" if dil == "Türkçe" else "Prostate Cancer"):
        gen = st.sidebar.selectbox(
            "Prostat Kanseri ile ilgili genler" if dil == "Türkçe" else "Prostate Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "BRCA2", "HOXB13", "ATM"]
        )
        if gen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Prostat Kanseri" if dil == "Türkçe" else "Prostate Cancer")
            st.write("Gen seçimi yaparak genetik bilgiler görüntüleyebilirsiniz." if dil == "Türkçe" else "Select a gene to view genetic information.")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak genler hakkında detaylı bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view detailed information.")
        elif gen == "BRCA2":
            st.header("BRCA2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "HOXB13":
            st.header("HOXB13")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gen == "ATM":
            st.header("ATM")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif kansertut == ("Kolorektal Kanser" if dil == "Türkçe" else "Colorectal Cancer"):
        kolorgen = st.sidebar.selectbox(
            "Kolorektal Kanser ile ilgili genler" if dil == "Türkçe" else "Colorectal Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "APC", "MLH1", "MSH2", "KRAS"]
        )
        if kolorgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Kolorektal Kanseri" if dil == "Türkçe" else "Colorectal Cancer")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak genler hakkında detaylı bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view detailed information.")
        elif kolorgen == "APC":
            st.header("APC")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif kolorgen == "MLH1":
            st.header("MLH1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif kolorgen == "MSH2":
            st.header("MSH2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif kolorgen == "KRAS":
            st.header("KRAS")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif kansertut == ("Akciğer Kanseri" if dil == "Türkçe" else "Lung Cancer"):
        akgen = st.sidebar.selectbox(
            "Akciğer Kanseri ile ilgili genler" if dil == "Türkçe" else "Lung Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "EGFR", "KRAS", "ALK", "TP53"]
        )
        if akgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Akciğer Kanseri" if dil == "Türkçe" else "Lung Cancer")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak genler hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view information.")
        elif akgen == "EGFR":
            st.header("EGFR")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif akgen == "KRAS":
            st.header("KRAS")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif akgen == "ALK":
            st.header("ALK")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif akgen == "TP53":
            st.header("TP53")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif kansertut == ("Pankreas Kanseri" if dil == "Türkçe" else "Pancreatic Cancer"):
        pangen = st.sidebar.selectbox(
            "Pankreas Kanseri ile ilgili genler" if dil == "Türkçe" else "Pancreatic Cancer related genes",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "BRCA2", "KRAS", "CDKN2A", "TP53"]
        )
        if pangen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Pankreas Kanseri" if dil == "Türkçe" else "Pancreatic Cancer")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Gen seçimi yaparak bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene to view information.")
        elif pangen == "BRCA2":
            st.header("BRCA2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif pangen == "KRAS":
            st.header("KRAS")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif pangen == "CDKN2A":
            st.header("CDKN2A")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif pangen == "TP53":
            st.header("TP53")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
elif kategori == ("Nörolojik Hastalıklar" if dil == "Türkçe" else "Neurological Diseases"):
    hastalık = st.sidebar.selectbox(
        "Hastalık Seçin" if dil == "Türkçe" else "Select Disease",
        [
            "Seçim Yapın" if dil == "Türkçe" else "Select",
            "Alzheimer",
            "Parkinson",
            "Huntington",
            "Amyotrofik Lateral Skleroz (ALS)" if dil == "Türkçe" else "Amyotrophic Lateral Sclerosis (ALS)",
            "Genetik Epilepsiler" if dil == "Türkçe" else "Genetic Epilepsies"
        ]
    )
    if hastalık == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
        st.header("Nörolojik Hastalıklar" if dil == "Türkçe" else "Neurological Diseases")
        st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastalık == "Alzheimer":
        alzgen = st.sidebar.selectbox(
            "Alzheimerla alakalı genler" if dil == "Türkçe" else "Genes related to Alzheimer",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "APP", "PSEN1", "PSEN2", "APOE"]
        )
        if alzgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Alzheimer")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Alzheimer ile alakalı gen seçerek gen hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Alzheimer to get information.")
        elif alzgen == "APP":
            st.header("APP")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif alzgen == "PSEN1":
            st.header("PSEN1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif alzgen == "PSEN2":
            st.header("PSEN2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif alzgen == "APOE":
            st.header("APOE")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastalık == "Parkinson":
        parkgen = st.sidebar.selectbox(
            "Parkinson hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Parkinson's disease",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "SNCA", "LRRK2", "PARK7", "PINK1"]
        )
        if parkgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Parkinson")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Parkinson hastalığı ile alakalı gen seçerek gen hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Parkinson's disease to get information.")
        elif parkgen == "SNCA":
            st.header("SNCA")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif parkgen == "LRRK2":
            st.header("LRRK2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif parkgen == "PARK7":
            st.header("PARK7")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif parkgen == "PINK1":
            st.header("PINK1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastalık == "Huntington":
        huntgen = st.sidebar.selectbox(
            "Huntington hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Huntington's disease",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "HTT"]
        )
        if huntgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Huntington")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Huntington hastalığı ile alakalı gen seçerek gen hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Huntington's disease to get information.")
        elif huntgen == "HTT":
            st.header("HTT")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastalık == ("Amyotrofik Lateral Skleroz (ALS)" if dil == "Türkçe" else "Amyotrophic Lateral Sclerosis (ALS)"):
        amfgen = st.sidebar.selectbox(
            "Amyotrofik Lateral Skleroz (ALS) hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to ALS",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "SOD1", "C9orf72", "TARDBP", "FUS"]
        )
        if amfgen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Amyotrofik Lateral Skleroz" if dil == "Türkçe" else "Amyotrophic Lateral Sclerosis")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Amyotrofik Lateral Skleroz (ALS) hastalığı ile alakalı gen seçerek gen hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to ALS to get information.")
        elif amfgen == "SOD1":
            st.header("SOD1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif amfgen == "C9orf72":
            st.header("C9orf72")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif amfgen == "TARDBP":
            st.header("TARDBP")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif amfgen == "FUS":
            st.header("FUS")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastalık == ("Genetik Epilepsiler" if dil == "Türkçe" else "Genetic Epilepsies"):
        epgen = st.sidebar.selectbox(
            "Epilepsi hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to epilepsy",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "SCN1A", "SCN2A", "KCNQ2", "CHRNA4"]
        )
        if epgen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Genetik Epilepsiler" if dil == "Türkçe" else "Genetic Epilepsies")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Epilepsi hastalığı ile alakalı gen seçerek gen hakkında bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to epilepsy to get information.")
        elif epgen == "SCN1A":
            st.header("SCN1A")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif epgen == "SCN2A":
            st.header("SCN2A")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif epgen == "KCNQ2":
            st.header("KCNQ2")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif epgen == "CHRNA4":
            st.header("CHRNA4")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
elif kategori == ("Kalıtsal Metabolik Hastalıklar" if dil == "Türkçe" else "Hereditary Metabolic Diseases"):
    hastur = st.sidebar.selectbox(
        "Kalıtsal Metabolik Hastalık Türleri" if dil == "Türkçe" else "Types of Hereditary Metabolic Diseases",
        [
            "Seçim yapın" if dil == "Türkçe" else "Select",
            "Fenilketonüri" if dil == "Türkçe" else "Phenylketonuria",
            "Galaktozemi" if dil == "Türkçe" else "Galactosemia",
            "Glikojen Depo Hastalıkları (Tip1)" if dil == "Türkçe" else "Glycogen Storage Diseases (Type 1)",
            "Mukopolisakkaridoz Tip 1 (MPS I)" if dil == "Türkçe" else "Mucopolysaccharidosis Type 1 (MPS I)",
            "Tay-Sachs Hastalığı" if dil == "Türkçe" else "Tay-Sachs Disease"
        ]
    )
    if hastur == ("Seçim yapın" if dil == "Türkçe" else "Select"):
        st.header("Kalıtsal Metabolik Hastalıklar" if dil == "Türkçe" else "Hereditary Metabolic Diseases")
        st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastur == ("Fenilketonüri" if dil == "Türkçe" else "Phenylketonuria"):
        fengen = st.sidebar.selectbox(
            "Fenilketonüri hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Phenylketonuria",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "PAH", "GCH1"]
        )
        if fengen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Fenilketonüri" if dil == "Türkçe" else "Phenylketonuria")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Fenilketonüri hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Phenylketonuria to get information.")
        elif fengen == "PAH":
            st.header("PAH")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif fengen == "GCH1":
            st.header("GCH1")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastur == ("Galaktozemi" if dil == "Türkçe" else "Galactosemia"):
        galagen = st.sidebar.selectbox(
            "Galaktozemi hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Galactosemia",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "GALT", "GALE", "GALM"]
        )
        if galagen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Galaktozemi" if dil == "Türkçe" else "Galactosemia")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Galaktozemi hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Galactosemia to get information.")
        elif galagen == "GALE":
            st.header("GALE")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif galagen == "GALM":
            st.header("GALM")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif galagen == "GALT":
            st.header("GALT")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastur == ("Glikojen Depo Hastalıkları (Tip1)" if dil == "Türkçe" else "Glycogen Storage Diseases (Type 1)"):
        gligen = st.sidebar.selectbox(
            "Glikojen Depo Hastalıkları (Tip1) ile alakalı genler" if dil == "Türkçe" else "Genes related to Glycogen Storage Diseases (Type 1)",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "G6PC", "SLC37A4"]
        )
        if gligen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Glikojen Depo Hastalıkları (Tip1)" if dil == "Türkçe" else "Glycogen Storage Diseases (Type 1)")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Glikojen Depo Hastalıkları (Tip1) hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Glycogen Storage Diseases (Type 1) to get information.")
        elif gligen == "G6PC":
            st.header("G6PC")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
        elif gligen == "SLC37A4":
            st.header("SLC37A4")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastur == ("Mukopolisakkaridoz Tip 1 (MPS I)" if dil == "Türkçe" else "Mucopolysaccharidosis Type 1 (MPS I)"):
        mugen = st.sidebar.selectbox(
            "Mukopolisakkaridoz Tip 1 (MPS I) hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Mucopolysaccharidosis Type 1 (MPS I)",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "IDUA"]
        )
        if mugen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Mukopolisakkaridoz Tip 1 (MPS I)" if dil == "Türkçe" else "Mucopolysaccharidosis Type 1 (MPS I)")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Mukopolisakkaridoz hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to MPS I to get information.")
        elif mugen == "IDUA":
            st.header("IDUA")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif hastur == ("Tay-Sachs Hastalığı" if dil == "Türkçe" else "Tay-Sachs Disease"):
        tagen = st.sidebar.selectbox(
            "Tay-Sachs Hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Tay-Sachs Disease",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "HEXA"]
        )
        if tagen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Tay-Sachs Hastalığı" if dil == "Türkçe" else "Tay-Sachs Disease")
            st.write("Bilgiler" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Tay-Sachs hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Tay-Sachs Disease to get information.")
elif kategori == ("Psikolojik Hastalıklar" if dil == "Türkçe" else "Psychiatric Disorders"):
    tur = st.sidebar.selectbox(
        "Psikolojik hastalık türleri" if dil == "Türkçe" else "Psychiatric Disorders",
        ["Seçim yapın" if dil == "Türkçe" else "Select",
         "Şizofreni" if dil == "Türkçe" else "Schizophrenia",
         "Bipolar Bozukluk" if dil == "Türkçe" else "Bipolar Disorder",
         "Depresyon" if dil == "Türkçe" else "Depression",
         "Otizm Spektrum Bozukluğu" if dil == "Türkçe" else "Autism Spectrum Disorder",
         "Dikkat Eksikliği ve Hiperaktivite Bozukluğu(DEHB / ADHD)" if dil == "Türkçe" else "Attention Deficit Hyperactivity Disorder (ADHD)"])
    if tur == ("Seçim yapın" if dil == "Türkçe" else "Select"):
        st.header("Psikolojik Hastalıklar" if dil == "Türkçe" else "Psychiatric Disorders")
        st.write("Bilgiler" if dil == "Türkçe" else "Information")
    elif tur == ("Şizofreni" if dil == "Türkçe" else "Schizophrenia"):
        sizgen = st.sidebar.selectbox(
            "Şizofreni hastalığı ile alakalı genler" if dil == "Türkçe" else "Genes related to Schizophrenia",
            ["Seçim Yapın" if dil == "Türkçe" else "Select", "COMT", "DISC1", "NRG1", "DTNBP1"]
        )
        if sizgen == ("Seçim Yapın" if dil == "Türkçe" else "Select"):
            st.header("Şizofreni Hastalığı" if dil == "Türkçe" else "Schizophrenia")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Şizofreni Hastalığı ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Schizophrenia to get information.")
        elif sizgen == "COMT":
            st.header("COMT")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif sizgen == "DISC1":
            st.header("DISC1")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif sizgen == "NRG1":
            st.header("NRG1")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif sizgen == "DTNBP1":
            st.header("DTNBP1")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
    elif tur == ("Bipolar Bozukluk" if dil == "Türkçe" else "Bipolar Disorder"):
        bigen = st.sidebar.selectbox(
            "Bipolar Bozukluk ile alakalı genler" if dil == "Türkçe" else "Bipolar Disorder",
            ["Seçim yapın" if dil == "Türkçe" else "Select","ANK3","CACNA1C","BDNF"]
        )
        if bigen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Bipolar Bozukluk" if dil == "Türkçe" else "Bipolar Disorder")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Bipolar Bozukluk ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Bipolar Disorder to get information.")
        elif bigen == "ANK3":
            st.header("ANK3")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif bigen == "CACNA1C":
            st.header("CACNA1C")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif bigen == "BDNF":
            st.header("BDNF")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
    elif tur == ("Depresyon" if dil == "Türkçe" else "Depression"):
        degen = st.sidebar.selectbox(
            "Depresyon ile alakalı genler" if dil == "Türkçe" else "Genes related to Depression",
            ["Seçim yapın" if dil == "Türkçe" else "Select","SLC6A4","BDNF","HTR2A"]
        )
        if degen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Depresyon" if dil == "Türkçe" else "Depression")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Depresyon ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Depression to get information.")
        elif degen == "SLC6A4":
            st.header("SLC6A4")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif degen == "BDNF":
            st.header("BDNF")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif degen == "HTR2A":
            st.header("HTR2A")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
    elif tur == ("Otizm Spektrum Bozukluğu" if dil == "Türkçe" else "Autism Spectrum Disorder"):
        ogen = st.sidebar.selectbox(
            "Otizm Spektrum Bozukluğu ile alakalı genler" if dil == "Türkçe" else "Genes related to Autism Spectrum Disorder",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "SHANK3","NRXN1","CHD8"]
        )
        if ogen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Otizm Spektrum Bozukluğu" if dil == "Türkçe" else "Autism Spectrum Disorder")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Otizm Spektrum Bozukluğu ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Autism Spectrum Disorder to get information.")
        elif ogen == "SHANK3":
            st.header("SHANK3")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif ogen == "NRXN1":
            st.header("NRG1")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif ogen == "CHD8":
            st.header("CHD8")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
    elif tur == ("Dikkat Eksikliği ve Hiperaktivite Bozukluğu(DEHB / ADHD)" if dil == "Türkçe" else "Attention Deficit Hyperactivity Disorder (ADHD)"):
        dgen = st.sidebar.selectbox(
            "Dikkat Eksikliği ve Hiperaktivite Bozukluğu ile alakalı genler" if dil == "Türkçe" else "Genes related to Attention Deficit Hyperactivity Disorder (ADHD)",
            ["Seçim yapın" if dil == "Türkçe" else "Select", "DRD4","SLC6A3","DAT1"]
        )
        if dgen == ("Seçim yapın" if dil == "Türkçe" else "Select"):
            st.header("Dikkat Eksikliği ve Hiperaktivite Bozukluğu(DEHB / ADHD)" if dil == "Türkçe" else "Attention Deficit Hyperactivity Disorder (ADHD)")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
            with st.sidebar:
                st.write("")
                st.write("Dikkat Eksikliği ve Hiperaktivite Bozukluğu ile alakalı gen seçerek bilgi alabilirsiniz." if dil == "Türkçe" else "Select a gene related to Attention Deficit Hyperactivity Disorder (ADHD) to get information.")
        elif dgen == "DRD4":
            st.header("DRD4")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif dgen == "SLC6A3":
            st.header("SLC6A3")
            st.write("Bilgi" if dil == "Türkçe" else "Information")
        elif dgen == "DAT1":
            st.header("DAT1")
            st.write("Bilgi" if dil == "Türkçe" else "Information")