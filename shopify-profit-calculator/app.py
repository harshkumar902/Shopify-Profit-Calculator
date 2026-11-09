import streamlit as st
st.set_page_config(page_title="Shopify Profit Calculator")
st.title("Shopify Profit Calculator")
st.caption("Contribution estimates exclude fixed overhead and tax unless included below.")
price=st.number_input("Selling price (₹)",0.0,100000.0,1200.0,step=50.0)
product=st.number_input("Product + packaging cost (₹)",0.0,100000.0,420.0,step=10.0)
shipping=st.number_input("Forward shipping (₹)",0.0,10000.0,75.0)
fee_pct=st.number_input("Payment/platform fees (%)",0.0,100.0,3.0)
ad_cac=st.number_input("Ad acquisition cost per order (₹)",0.0,100000.0,280.0)
cod_rate=st.slider("COD share (%)",0,100,40)
rto_rate=st.slider("RTO among COD orders (%)",0,100,15)
rto_cost=st.number_input("Extra loss per returned COD order (₹)",0.0,10000.0,150.0)
fees=price*fee_pct/100
expected_rto=cod_rate/100*rto_rate/100*rto_cost
contribution=price-product-shipping-fees-ad_cac-expected_rto
pre_ad=price-product-shipping-fees-expected_rto
c1,c2,c3=st.columns(3)
c1.metric("Expected contribution / order",f"₹{contribution:,.2f}")
c2.metric("Contribution margin",f"{contribution/price*100:.1f}%" if price else "N/A")
c3.metric("Break-even ROAS",f"{price/pre_ad:.2f}x" if pre_ad>0 else "Not achievable")
st.write("Expected RTO loss per placed order:",f"₹{expected_rto:,.2f}")
st.caption("Simplification: RTO cost is additional loss, weighted by COD and RTO rates. Realized revenue, refunds, GST and return accounting require a fuller model.")
