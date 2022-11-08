import gradio as gr
import pickle

# Terdapat 7 parameter yang perlu diinput:
# Pemerataan Layanan Perpustakaan
# Ketercukupan Koleksi Perpustakaan
# Ketercukupan Tenaga Perpustakaan
# Tingkat Kunjungan Masyarakat per Hari
# Perpustakaan ber-SNP
# Keterlibatan Masyarakat dalam KIE
# Anggota Perpustakaan
# Output prediksi=indeks literatur


def make_pred(plp, kkp, ktp, tkmph, psnp, kmk, ap):
    with open("model_iplm.pkl", "rb") as f:
        model = pickle.load(f)
        preds = model.predict([[plp, kkp, ktp, tkmph, psnp, kmk, ap]])
    if preds:
        return "Indeks Literatur tinggi (1)"
    return "Indeks Literatur rendah (0)"


plp_i = gr.Number(label="Pemerataan Layanan Perpustakaan")
kkp_i = gr.Number(label="Ketercukupan Koleksi Perpustakaan")
ktp_i = gr.Number(label="Ketercukupan Tenaga Perpustakaan")
tkmph_i = gr.Number(label="Tingkat Kunjungan Masyarakat per Hari")
psnp_i = gr.Number(label="Perpustakaan ber-SNP")
kmk_i = gr.Number(label="Keterlibatan Masyarakat dalam KIE")
ap_i = gr.Number(label="Anggota Perpustakaan")

output = gr.Textbox()

app = gr.Interface(fn=make_pred, inputs=[
                   plp_i, kkp_i, ktp_i, tkmph_i, psnp_i, kmk_i, ap_i], outputs=output)
app.launch()
