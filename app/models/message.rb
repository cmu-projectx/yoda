class Message < ActiveRecord::Base
  attr_accessible :body, :date, :sender, :subject, :to
end
