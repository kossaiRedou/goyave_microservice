from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .db import Base

class Produit(Base):
    __tablename__ = "produits"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, index=True)
    nom = Column(String)
    stock_minimum = Column(Integer)

class Vente(Base):
    __tablename__ = "ventes"
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey("produits.id"), index=True)
    date = Column(Date)
    quantite = Column(Integer)

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey("produits.id"), index=True)
    date = Column(Date)
    quantite = Column(Integer)

class Prediction(Base):
    __tablename__ = "model_predictions"
    produit_id = Column(Integer, ForeignKey("produits.id"), primary_key=True)
    date_prediction = Column(Date, primary_key=True)
    duree_stock = Column(String, primary_key=True)
    jours_avant_rupture = Column(Integer)
    quantite_duree_stock = Column(Integer)
